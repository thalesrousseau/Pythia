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
    database = program_path()

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
