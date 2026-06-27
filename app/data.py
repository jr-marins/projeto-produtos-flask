'''
Módulo responsável por fornecer os dados dos produtos.
'''

import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent # Caminho para o diretório do projeto
ARQUIVO_JSON = base_dir / 'produtos.json'  # Caminho para o arquivo JSON

def get_produtos():
    """
    Retorna uma lista de produtos a partir do arquivo JSON.
    """
    try:
        with open(
            ARQUIVO_JSON,
            'r',
            encoding='utf-8',
            ) as file:
            
            produtos = json.load(file)
            return produtos
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def salvar_produtos(produtos):
    """
    Salva a lista de produtos no arquivo JSON.
    """
    with open(
        ARQUIVO_JSON,
         'w',
         encoding='utf-8'
         ) as file:
        
        json.dump(
            produtos,
            file,
            ensure_ascii=False,
            indent=4
            )