"""Module to handle mail server functionalities."""

# MAIL_SERVICE #
#
# Importing libraries
import base64
import mimetypes
import json
from email.message import EmailMessage

# Importing modules
<<<<<<< HEAD
from Google_Server import connect_server
from Program_Variables import program_files
from Program_Variables import admin_login
=======
from Program_Variables import program_files
>>>>>>> 04837fcaaaea258527f0c0af1d7fa5d0bc2b5a29
from Event_Logs import write_log


# Creating 'create_message' function
<<<<<<< HEAD
def create_message(TO, SUBJECT, MESSAGE_TEXT, FILE):
=======
def create_message(SENDER, TO, SUBJECT, MESSAGE_TEXT, FILE):
>>>>>>> 04837fcaaaea258527f0c0af1d7fa5d0bc2b5a29
    """Create a message for an email.

    Args:
        SENDER: A string with email address of the sender.
        TO: An array with string of email address(es) of the receiver(s).
        SUBJECT: A string with the subject of the email message.
        MESSAGE_TEXT: A string with the text of the email message.
        FILE: A string with the path to the file to be attached.

    Returns:
        An object containing a base64url decoded email object.
    """
    # Creating 'MIME' instance to store the email message
    message = EmailMessage()

    # Writing email attributes
    message['To'] = ', '.join(TO)
<<<<<<< HEAD
    message['From'] = admin_login()
=======
    message['From'] = SENDER
>>>>>>> 04837fcaaaea258527f0c0af1d7fa5d0bc2b5a29
    message['Subject'] = SUBJECT

    # Writing email message
    message_text = MESSAGE_TEXT
    message.set_content(message_text)
    write_log('Mensagem de email criada')

    # Checking for attachment
    content = bool(FILE)
    if content is True:

        # Using loop to attach more than one file
        for file in FILE:

            # Determining file format
            mime_type, _ = mimetypes.guess_type(file)
            mime_type, mime_subtype = mime_type.split('/')

            # Getting file for attachment
<<<<<<< HEAD
            with open(f'{program_files()}/{file}', 'rb') as attachment:
=======
            with open(f'{program_files()}/Files/{file}', 'rb') as attachment:
>>>>>>> 04837fcaaaea258527f0c0af1d7fa5d0bc2b5a29

                # Attaching files
                message.add_attachment(attachment.read(), maintype=mime_type,
                                       subtype=mime_subtype, filename=file)
<<<<<<< HEAD
                write_log('Arquivo anexado a mensagem')
=======
                write_log(f'Arquivo "{file}" anexado')
>>>>>>> 04837fcaaaea258527f0c0af1d7fa5d0bc2b5a29

        # Encoding email message in 'base64'
    raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))

    # Exporting decoded email message
    return {'raw': raw_message.decode("utf-8")}


# Creating 'send_email' function
<<<<<<< HEAD
def send_email(SUBJECT, MESSAGE):
=======
def send_email(SERVICE_SESSION, SUBJECT, MESSAGE):
>>>>>>> 04837fcaaaea258527f0c0af1d7fa5d0bc2b5a29
    """Send an email message.

    Args:
      SERVICE_SESSION: An object containing a running service session.
      SUBJECT: A string with subject of the email message.
      MESSAGE: An object containing a base64url decoded email object.

    Returns:
      Sent email message.
    """
<<<<<<< HEAD
    # Creating a session on the server
    api_service = 'gmail'
    api_version = 'v1'
    scopes = ['https://mail.google.com/']
    server_session = connect_server(api_service, api_version, scopes)

    # Sending email message
    try:
        message = server_session.users().messages().send(
=======
    # Sending email message
    try:
        message = SERVICE_SESSION.users().messages().send(
>>>>>>> 04837fcaaaea258527f0c0af1d7fa5d0bc2b5a29
            userId='me', body=MESSAGE).execute()
        write_log('Mensagem de email enviada')
        write_log('Código da mensagem: "%s"' % message['id'])
        return message

        # Exception when the email message cannot be sent
    except Exception as error:
        write_log(f'Um erro ocorreu ao enviar a mensagem de email "{SUBJECT}"')
        reason = json.loads(error.content).get('error').get('errors')[0].get(
            'reason')
        write_log(f'Razão: "{reason}"')
        return None
