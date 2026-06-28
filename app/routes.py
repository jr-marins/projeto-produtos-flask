'''
esse modulo contém as rotas da aplicação.
As rotas são definidas usando o Blueprint do Flask,
que permite organizar as rotas em módulos separados.
o Blueprint é registrado na aplicação Flask no arquivo
__init__.py, permitindo que as rotas sejam acessadas quando
a aplicação é executada.
'''

from flask import Blueprint, render_template, request, redirect
from .services import listar_produtos, adicionar_produto, buscar_produto_por_id

bp = Blueprint("produtos", __name__)
''' 
Blueprint para as rotas principais da aplicação.
'''

@bp.route("/produtos", methods=["GET", "POST"])
def produtos():
    '''
    Rota para exibir a lista de produtos.
    '''
    if request.method == "POST":

        nome = request.form["nome"]
        preco = float(request.form["preco"])

        
        adicionar_produto(nome, preco)# Função fictícia para adicionar o produto

        return redirect("/produtos")  # Redireciona para a mesma página após adicionar o produto
    
    produtos = listar_produtos()
    return render_template(
        "produtos.html",
        produtos=produtos
    )


'''
produtos.html é um template HTML que será renderizado
quando a rota /produtos for acessada. Ele recebe a lista
de produtos como contexto e exibe os produtos na página.

produtos=produtos é um argumento passado para o template, permitindo
que a lista de produtos seja acessada dentro do template.

'''

# rota para editar produtos
@bp.route("/produtos/<int:produto_id>/editar", methods=["GET", "POST"])
def editar_produto_route(produto_id):
    """
    rota para editar um produto existente.
    """
    produto = buscar_produto_por_id(listar_produtos(), produto_id)]

    return render_template(
        "editarP.html",
        produto=produto
    )
