"""."""


# Assets_Database #
#
# Importing libraries
import requests
import zipfile
import pandas
from io import BytesIO

# Importing modules
from Event_Logs import write_log
from Program_Variables import program_path


def update_database():
<<<<<<< HEAD:modules/Assets_Database.py
    database = program_path()
=======
    """."""
    # Getting variable 'HOME'
    database = program_path() + '/resources'
>>>>>>> d4f47740da4240fffd623f97fe6e43581887cbdb:pythia/Stock_Database.py

    url = 'https://bvmf.bmfbovespa.com.br/InstDados/InformacoesEmpresas/ClassifSetorial.zip'
    content = BytesIO(requests.get(url, verify=False).content)
    zipdata = zipfile.ZipFile(content)
    zipname = zipdata.namelist()
    # zipdata.extractall(database)
    # dataframe = pandas.read_excel(f'{database}/{zipname[0]}')
    b = print(database)
    return(b)


a = update_database()
# fundos
# https://sistemaswebb3-listados.b3.com.br/fundsPage/7
