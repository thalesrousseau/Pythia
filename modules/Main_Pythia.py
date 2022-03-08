"""Module to."""

# MAIN_PYTHIA #
#
# Importing libraries
import os

# Importing modules
from Event_Logs import write_log

# Getting variable 'HOME'
files = os.environ.get('HOME') + '/pythia'

# Creating a folder to store analysis files
if not os.path.exists(files):
    os.mkdir(files)
    write_log('Pasta PYTHIA criada em HOME')
