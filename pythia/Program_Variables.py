"""Module to store string variables used many times through the program."""

# PROGRAM_VARIABLES #
#
# Importing libraries
import os

# Importing modules
from Event_Logs import write_log


# Creating 'program_path' function
def program_path():
    """Export the path where the program is installed.

    Returns:
    An object containing a string with the path to the program.
    """
    # Getting variable PATH
    path = os.getcwd()
    write_log("Variável PROGRAM_PATH importada")

    # Exporting variable 'PATH'
    return(path)


# Creating 'program_files' function
def program_folder():
    """Export the path where the program files are stored.

    Returns:
    An object containing a string with the path to the files.
    """
    # Getting variable 'HOME'
    files = os.environ.get('HOME') + '/Pythia'

    # Exporting variable 'FILES'
    write_log('Variável PROGRAM_FILES importada')
    return(files)


# Creating 'admin_login' function
def admin_login():
    """Export the internet identifier used in services authentication.

    Returns:
    An object containing a string with identifier.
    """
    # Getting variable 'PYTHIA_LOGIN'
    login = os.environ.get('PYTHIA_LOGIN')
    if not os.path.exists(login):
        write_log('Variável PYTHIA_LOGIN não designada')

    # Exporting variable 'PYTHIA_LOGIN'
    else:
        write_log('Variável PYTHIA_LOGIN importada')
        return(login)


# Creating 'admin_passwd' function
def admin_passwd():
    """Export the internet password used in services authentication.

    Returns:
    An object containing a string with password.
    """
    # Getting variable 'PYTHIA_PASSWD'
    token = os.environ.get('PYTHIA_PASSWD')
    if not os.path.exists(token):
        write_log('Variável PYTHIA_PASSWD não designada')

    # Exporting variable 'PYTHIA_PASSWD'
    else:
        write_log('Variável PYTHIA_PASSWD importada')
        return(token)
