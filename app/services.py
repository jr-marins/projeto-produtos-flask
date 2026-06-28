'''
serviços para manipulação de dados dos produtos.
'''

from .data import get_produtos, salvar_produtos


def listar_produtos():

    '''
    Função para listar os produtos.
    Retorna a lista de produtos obtida da função get_produtos().
    '''
    return get_produtos()

def validar_produto(nome, preco):
    '''
    Função para validar os dados do produto.
    Recebe o nome e o preço do produto como parâmetros.
    Retorna True se os dados forem válidos, caso contrário, retorna False.
    '''
    # Regras de validação para o nome e preço do produto
    # Normaliza o nome do produto removendo espaços em branco no início e no final
    
    if not nome or not isinstance(nome, str):
        return False
    
    nome = nome.strip()  
    
    if not isinstance(preco, (int, float)) or preco <= 0:
        return False

    return True


# com os dados validados, podemos adicionar o produto
def adicionar_produto(nome, preco):
    '''
    Função para adicionar um novo produto.
    Recebe o nome e o preço do produto como parâmetros.
    Aqui você pode implementar a lógica para salvar o produto no banco de dados.
    '''

    # aqui chamamos a função validar_produto para verificar se os dados são válidos
    if not validar_produto(nome, preco):
        raise ValueError("Dados do produto inválidos." \
        "Certifique-se de que o nome seja uma string não vazia" \
        "e o preço seja um número positivo.")
    
    
    produtos = get_produtos()

    novo_produto = {

        "id": len(produtos) + 1,
        "nome": nome,
        "preco": preco,

        }  # Cria um novo produto
    
    # agora salvasmos o novo produto no arquivo JSON
    produtos.append(novo_produto)
    salvar_produtos(produtos)

"""
função para buscar um produto pelo ID.
"""

def buscar_produto_por_id(produto_id):
    produtos = get_produtos()
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return None