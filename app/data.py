'''
Módulo responsável por fornecer os dados dos produtos.
'''

import json

def get_produtos():
    """
    Retorna uma lista de produtos a partir do arquivo JSON.
    """
    try:
        with open(
            'produtos.json',
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
        'produtos.json',
         'w',
         encoding='utf-8'
         ) as file:
        
        json.dump(
            produtos,
            file,
            ensure_ascii=False,
            indent=4
            )