import csv
import json
from datetime import datetime

from fastapi import APIRouter

router = APIRouter(prefix='/pacotes')


@router.get('/')
def listar_pacotes_em_ordem(ordem: str = 'nome'):
    dados = abrir_arquivo()

    match ordem:
        case 'versao':
            dados_ord = sorted(dados, key=lambda x: x['Versao'])
        case 'data':
            dados_ord = sorted(dados, key=lambda x: datetime.strptime(x['Data'], '%d-%m-%Y'))
        case _:
            dados_ord = sorted(dados, key=lambda x: x['Nome'])

    json_data = json.dumps(dados_ord, ensure_ascii=False)
    return json_data


@router.get('/nome/{nome}')
def listar_pacotes_por_nome(nome: str):
    dados = abrir_arquivo()

    nomes = list(filter(lambda x: x['Nome'] == nome, dados))
    json_data = json.dumps(nomes, ensure_ascii=False)
    return json_data


@router.get('/versao/{versao}')
def listar_pacotes_por_versao(versao: str):
    dados = abrir_arquivo()
    print(versao)
    versoes = list(filter(lambda x: x['Versao'] == versao, dados))
    json_data = json.dumps(versoes, ensure_ascii=False)
    return json_data


def abrir_arquivo():
    with open('pacotes.csv', 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        leitor_csv.__next__()
        dados = list(leitor_csv)

    return dados


