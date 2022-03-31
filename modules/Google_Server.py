"""Module to start a server session."""

# GOOGLE_SERVER #
#
# Importing libraries
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Importing modules
from Program_Variables import program_path
from Event_Logs import write_log


# Creating 'connect_server' function
def connect_server(API_SERVICE, API_VERSION, SCOPES):
    """Start a server session.

    Args:
    API_SERVICE: A string with the API service to be acessed by the program.
    API_VERSION: A string with the running version of the API service.
    SCOPES: A string with the scopes that will be acessed by the program.

    Returns:
    An object containing a running service session.
    """
    # Creating variable to store credentials
    certificate = None

    # Searching for 'token' file
    token = f'{program_path()}/resources/token_{API_SERVICE}_{API_VERSION}.json'
    if os.path.exists(token):

        # Fetching program credentials within 'token' file
        certificate = Credentials.from_authorized_user_file(token, SCOPES)
        write_log('Buscando credenciais de acesso ao servidor')

    # Validating credentials
    if not certificate or not certificate.valid:
        write_log('Acesso ao servidor negado')

        # Replacing expired credentials
        if certificate and certificate.expired and certificate.refresh_token:
            try:
                certificate.refresh(Request())
                write_log('Credenciais de acesso ao servidor renovadas')

            except Exception as error:
                write_log('Sessão no servidor não pode ser criada')
                write_log(f'[ERRO]: {error.args[0]}')

                # Deleting 'token' file
                os.remove(token)
                write_log('Arquivo TOKEN excluído')

        # Redirecting to manual authentication
        if not os.path.exists(token):
            flow = InstalledAppFlow.from_client_secrets_file(
                'resources/credentials.json', SCOPES)
            certificate = flow.run_local_server(port=0)
            write_log('Autenticação manual realizada no servidor')

        # Creating an authentication 'token' file
        with open(token, 'w') as file:
            file.write(certificate.to_json())
            write_log('Arquivo de credenciais de acesso ao servidor criadas')

    # Initianting session on server
    try:
        service = build(API_SERVICE, API_VERSION, credentials=certificate)
        write_log('Sessão no servidor criada')
        return(service)

    # Exception when server session cannot be created
    except Exception as error:
        write_log('Sessão no servidor não pode ser criada')
        reason = json.loads(error.content).get('error').get('errors')[0].get(
            'reason')
        write_log(f'[ERRO]: {reason}')
