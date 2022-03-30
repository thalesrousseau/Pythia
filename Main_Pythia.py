"""Module to."""

# MAIN_PYTHIA #
#
# Importing libraries
import os

# Importing modules
from Event_Logs import write_log
from Program_Variables import program_path
from Program_Variables import program_folder

# Creating path to 'RESOURCES' folder
resources_folder = program_path() + '/resources'

# Creating a folder to store runtime files
if not os.path.exists(resources_folder):
    os.mkdir(resources_folder)
    write_log('Pasta PYTHIA criada em /HOME')

# Creating path to 'PYTHIA' folder
pythia_folder = program_folder()

# Creating a folder to store analysis files
if not os.path.exists(pythia_folder):
    os.mkdir(pythia_folder)
    write_log('Pasta PYTHIA criada em /HOME')
