"""."""

# Stock_Database #
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
    """."""
    # Getting variable 'HOME'
    database = program_path() + '/database'

    url = 'https://bvmf.bmfbovespa.com.br/InstDados/InformacoesEmpresas/ClassifSetorial.zip'
    content = BytesIO(requests.get(url, verify=False).content)
    zipdata = zipfile.ZipFile(content)
    zipinfo = zipdata.infolist()
    zipdata.extractall(database)
    # data = pandas.read_excel(zipinfo)


a = program_path()
print(a)
