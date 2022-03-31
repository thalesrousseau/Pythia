"""Module to handle cloud storage server functionalities."""

# CLOUD_SERVICE #
#
# Importing libraries
import json
import mimetypes
from apiclient.http import MediaFileUpload

# Importing modules
from Program_Variables import program_folder
from Google_Server import connect_server
from Event_Logs import write_log


# Creating 'search_archive' function
def search_drive(ARCHIVE):
    """Search for an archive within cloud storage service.

    Args:
        SERVICE_SESSION: An object containing a running service session.
        ARCHIVE_NAME: A string with the name of the archive to be finded.

    Returns:
        A tuple with a boolean value, an integer and a list of archive
        identification code.
    """
    # Creating a session on the server
    api_service = 'drive'
    api_version = 'v3'
    scopes = ['https://www.googleapis.com/auth/drive']
    server_session = connect_server(api_service, api_version, scopes)

    # Searching for file by name
    response = server_session.files().list(q=f"name='{ARCHIVE}'",
                                           fields='nextPageToken, files(id)',
                                           pageToken=None).execute()
    write_log(f'Busca por arquivo "{ARCHIVE}"')

    # Getting search result
    archives = response.get('files', [])

    # Checking for a positive result
    if not archives:
        write_log(f'Nenhum arquivo com nome "{ARCHIVE}" encontrado')
        return (False, 0, [None])

    # Returning request with file identifiers
    else:
        items = len(archives)
        write_log(f'{items} arquivo(s) com nome "{ARCHIVE}" encontrado')
        archives_identification = []
        for archive in archives:
            archives_identification.append(archive.get('id'))
        return (True, items, archives_identification)


# Creating 'create_folder' function
def create_folder(PARENT_DIRECTORY, FOLDER):
    """Create a folder within the cloud storage service in the designated path.

    Args:
        SERVICE_SESSION: An object containing a running service session.
        PARENT_DIRECTORY: A string with the parent directory of the folder to
        be created.
        FOLDER: A string with the name of the folder to be created.

    Returns:
        A created folder within cloud service.
    """
    # Creating a session on the server
    api_service = 'drive'
    api_version = 'v3'
    scopes = ['https://www.googleapis.com/auth/drive']
    server_session = connect_server(api_service, api_version, scopes)

    # Setting metadata for the folder created in the root directory
    if PARENT_DIRECTORY != 'Drive':
        folder_code = search_drive(server_session, PARENT_DIRECTORY)
        if folder_code[0] is True:
            folder_metadata = {'name': f'{FOLDER}',
                               'parents': [f'{folder_code[2][-1]}'],
                               'mimeType': 'application/vnd.google-apps.folder'
                               }

    # Setting folder metadata inside a parent directory
    if PARENT_DIRECTORY == 'Drive' or folder_code is False:
        folder_metadata = {'name': f'{FOLDER}',
                           'mimeType': 'application/vnd.google-apps.folder'}

    # Creating folder
    try:
        folder = server_session.files().create(
            body=folder_metadata, fields='id').execute()
        write_log(
            f'Pasta "{FOLDER}" criada dentro "{PARENT_DIRECTORY}"')
        write_log('Código da pasta: "%s"' % folder.get('id'))
        return folder

    # Exception when the folder cannot be created
    except Exception as error:
        write_log(f'Pasta "{FOLDER}" não pode ser criada')
        reason = json.loads(error.content).get('error').get('errors')[0].get(
            'reason')
        write_log(f'Razão: "{reason}"')


def upload_file(PARENT_DIRECTORY, FILE):
    """Upload a file within the parent directory inside cloud storage service.

    Args:
        SERVICE_SESSION: An object containing a running service session.
        PARENT_DIRECTORY: A string with the parent directory of the file to
        be uploaded.
        FILE: A string with the name of the file to be uploaded.
    """
    # Creating a session on the server
    api_service = 'drive'
    api_version = 'v3'
    scopes = ['https://www.googleapis.com/auth/drive']
    server_session = connect_server(api_service, api_version, scopes)

    # Determining file format
    mime_type, _ = mimetypes.guess_type(FILE)
    mime_type, mime_subtype = mime_type.split('/')

    # Setting metadata of file to be uploaded to root directory
    if PARENT_DIRECTORY != 'Drive':
        folder_code = search_drive(PARENT_DIRECTORY)
        if folder_code[0] is True:
            file_metadata = {'name': f'{FILE}',
                             'parents': [f'{folder_code[2][0]}'],
                             'mimeType': mime_type}

    # Setting metadata of file to be uploaded to parent directory
    if PARENT_DIRECTORY == 'Drive' or folder_code is False:
        file_metadata = {'name': f'{FILE}',
                         'mimeType': mime_type}

    # Getting file location
    media = MediaFileUpload(f'{program_folder()}/{FILE}',
                            mimetype=f'{mime_type}/{mime_subtype}')
    # Uploading the file to the cloud

    try:
        file = server_session.files().create(body=file_metadata,
                                             media_body=media,
                                             fields='id').execute()
        write_log('Arquivo carregado para nuvem\n'
                  f'Código do arquivo: {file.get("id")}')

    except Exception as error:
        write_log(f'Arquivo "{FILE}" não pode ser carregado para nuvem')
        reason = json.loads(error.content).get('error').get('errors')[0].get(
            'reason')
        write_log(f'Razão: "{reason}"')
