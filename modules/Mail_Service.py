"""Module to handle mail server functionalities."""

# MAIL_SERVICE #
#
# Importing libraries
import base64
import mimetypes
import json
from email.message import EmailMessage

# Importing modules
from Program_Variables import program_files
from Event_Logs import write_log


# Creating 'create_message' function
def create_message(SENDER, TO, SUBJECT, MESSAGE_TEXT, FILE):
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
    message['From'] = SENDER
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
            with open(f'{program_files()}/Files/{file}', 'rb') as attachment:

                # Attaching files
                message.add_attachment(attachment.read(), maintype=mime_type,
                                       subtype=mime_subtype, filename=file)
                write_log(f'Arquivo "{file}" anexado')

        # Encoding email message in 'base64'
    raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))

    # Exporting decoded email message
    return {'raw': raw_message.decode("utf-8")}


# Creating 'send_email' function
def send_email(SERVICE_SESSION, SUBJECT, MESSAGE):
    """Send an email message.

    Args:
      SERVICE_SESSION: An object containing a running service session.
      SUBJECT: A string with subject of the email message.
      MESSAGE: An object containing a base64url decoded email object.

    Returns:
      Sent email message.
    """
    # Sending email message
    try:
        message = SERVICE_SESSION.users().messages().send(
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
