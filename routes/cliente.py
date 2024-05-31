from flask import Blueprint, render_template, request
from database.models.cliente import Cliente


cliente_route = Blueprint("cliente", __name__)


"""
    Parece que esse barra que colocamos dentro do .route (.route("/")) vai conflitar com o / que colocamos dentro do home, mas naverdade nós vamos adicionar daqui a pouco uma funcionalidade que faça com que sempre inicie com /cilentes, e esse barra seria /clientes/, ou seja, a própria rota clientes
"""


"""
    <int:cliente_id> // Isso é uma rota dinâmica, ela vai acessar o id de cada usuário 
    Temos que indicar o tipo de dado e o nome que você queira

    Rota de Clientes

    - /clientes/ (GET)- listar os clientes
    - clientes/ (POST) - inserir o cliente no servidor
    - /clientes/new (GET) - renderizar o formulário para criar um cliente
    - /clientes/<id> (GET)- obter os dados de um cliente
    - /clientes/<id>/edit (GET)- renderizar um formulário para editar um cliente
    - /clientes/<id>/update (PUT- atualizar os dados do cliente
    - /clientes/<id>/delete (DELETE) - Deletar o registro de um usuário
"""

@cliente_route.route("/")
def lista_clientes():
    """ Listar os clientes """
    clientes = Cliente.select()
    return render_template("lista_clientes.html", clientes=clientes)


@cliente_route.route("/", methods=["POST"])
def inserir_cliente():
    """ Inserir os dados do cliente no banco de dados """
    
    data = request.json
    novo_usuario = Cliente.create(
        nome = data["nome"],
        email = data["email"],
    )

    return render_template("item_cliente.html", cliente=novo_usuario)


@cliente_route.route("/new")
def form_cliente():
    """ Formulário para cadastrar um cliente """
    return render_template("form_cliente.html")


@cliente_route.route("/<int:cliente_id>")
def detalhes_cliente(cliente_id):
    
    cliente = Cliente.get_by_id(cliente_id)

    return render_template("detalhe_cliente.html", cliente=cliente)


@cliente_route.route("/<int:cliente_id>/edit")
def form_edit_cliente(cliente_id):
    """ Formulário para editar o cliente """
    cliente = Cliente.get_by_id(cliente_id) 

    return render_template("form_cliente.html", cliente=cliente)


@cliente_route.route("/<int:cliente_id>/update", methods=["PUT"])
def atualizar_cliente(cliente_id):
    """ Atualizar informações do cliente """
    
    cliente_atualizado = request.json
    cliente_atualizado["id"] = cliente_id

    cliente = Cliente.get_by_id(cliente_id)
    cliente.nome = cliente_atualizado["nome"]
    cliente.email = cliente_atualizado["email"]
    cliente.save()

    return render_template('item_cliente.html', cliente=cliente_atualizado)


@cliente_route.route("/<int:cliente_id>/delete", methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ Deletar cliente do banco de dados """
    cliente = Cliente.get(Cliente.id == cliente_id)
    cliente.delete_instance()

    return {"deleted": "ok"}