"""Module to store string variables used many times through the program."""

# VARIABLES #
#
# Importing libraries
import os

# Importing modules
from Log import log


# Creating 'path' function
def path():
    """Export the path where the program is installed.

    Returns:
    An object containing a string with the path to the program.
    """
    # Getting variable PATH
    path = os.getcwd()
    log("Variável PATH importada")

    # Exporting variable 'PATH'
    return(path)


# Creating 'files' function
def files():
    """Export the path where the program files are stored.

    Returns:
    An object containing a string with the path to the files.
    """
    # Getting variable 'HOME'
    files = f"{os.environ('HOME')}/pythia"

    # Creating a folder to store analysis files
    if not os.path.exists(files):
        os.mkdir(f"{files}/pythia")
    log('Variável FILES importada')

    # Exporting variable 'FILES'
    return(files)


# Creating 'program_identifier' function
def identifier():
    """Export the internet identifier used in services authentication.

    Returns:
    An object containing a string with identifier.
    """
    # Getting variable 'IDENTIFIER'
    identifier = os.environ.get('PYTHIA_ID')
    if not os.path.exists(identifier):
        log('Variável IDENTIFIER não designada')

    # Exporting variable 'IDENTIFIER'
    else:
        log('Variável IDENTIFIER importada')
        return(identifier)


# Creating 'token' function
def token():
    """Export the internet password used in services authentication.

    Returns:
    An object containing a string with password.
    """
    # Getting variable 'PYTHIA_TOKEN'
    token = os.environ.get('PYHTIA_TOKEN')
    if not os.path.exists(token):
        log('Variável TOKEN não designada')

    # Exporting variable 'TOKEN'
    else:
        log('Variável TOKEN importada')
        return(token)
