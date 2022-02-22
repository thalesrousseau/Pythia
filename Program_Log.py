"""Module to save messages in a log file."""

# PROGRAM_LOG #
#
# Importing libraries
import datetime
import os.path

# Importing Module
from Environment_Variables import program_path


# Creating 'system_log' function
def program_log(MESSAGE):
    """Save a string message with date and time in log file.

    Args:
        MESSAGE: A string message to be saved.
    """
    # Getting time and hour
    date_time = datetime.datetime.now()
    date = date_time.strftime('%Y.%m.%d')
    time = date_time.strftime('%X')

    # Creating a folder to store log files
    if not os.path.exists(f'{program_path()}/logs'):
        os.mkdir(f'{program_path()}/logs')

    # Writing the Log file
    with open(f'{program_path()}/logs/[{date}] - pythia log.txt', 'a') as file:
        file.write(f'[{time}] - {MESSAGE}\n')
