from collections import OrderedDict

import uvicorn
from fastapi import FastAPI
from httpx import AsyncClient
from asyncio import run
from aiometer import run_all
from functools import partial
import csv
import os
from datetime import datetime

from router import pacote_router

app = FastAPI()

pacotes = ['requests', 'django', 'numpy', 'flask', 'pandas', 'matplotlib',
           'scikit-learn', 'tensorflow', 'keras', 'nltk',
           'beautifulsoup4', 'sqlalchemy', 'seaborn', 'scipy', 'opencv-python',
           'pytorch', 'pillow', 'networkx', 'gensim', 'pytz',
           'pytest', 'pyyaml', 'pymongo', 'sympy', 'bokeh',
           'plotly', 'scapy', 'jupyter', 'virtualenv', 'twilio',
           'pyautogui', 'tweepy', 'pyinstaller', 'pygame', 'openpyxl',
           'pyodbc', 'xlrd', 'xlwt', 'pyarrow', 'boto3',
           'paramiko', 'flask-restful', 'pyqt5', 'pycrypto', 'pydantic',
           'django-rest-framework', 'pysocks', 'docx', 'pygments', 'praw']

dados = []


async def req(pacote):
    '''
    Faz as requisições para a API do pypi de forma assincrona
    :param:  Nome do pacote que vai ser pesquisado:
    :return: Uma lista de tuplas com os dados que vieram da API
    '''
    async with AsyncClient(base_url='https://pypi.org/pypi/') as client:
        response = await client.get(f'{pacote}/json')

        version = response.json().get('info').get('version')
        data = response.json().get('releases').get(version)
        version_python = response.json().get('urls')[0].get('requires_python')
        data_version = datetime.fromisoformat(data[len(data)-1].get('upload_time')).strftime("%d-%m-%Y")

        dados.append((pacote, str(version_python).replace('>', '').replace('=', ''), data_version))


async def main_req():
    """
    Método feito para limitar a quantidade de requisições por segundo
     e não sobrecarregar a API, e também faz a escrita do arquivo CSV
    :return: Arquivo CSV com os dados preenchidos
    """
    if os.path.isfile('pacotes.csv'):
        return
    result = run_all([partial(req, pacote) for pacote in pacotes], max_at_once=5, max_per_second=10)
    await result
    with open('pacotes.csv', 'a', newline='') as arquivo_csv:
        cabecalho = OrderedDict([
            ('Nome', None),
            ('Versao', None),
            ('Data', None)
        ])

        pacotes_csv = csv.writer(arquivo_csv)
        pacotes_csv.writerow(cabecalho)
        for d in dados:
            pacotes_csv.writerow(d)

# Inicia o método
run(main_req())

app.include_router(pacote_router.router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8001)


