from model.database import query
import json

async def get_info_product():
    """
    Retorna as informações dos produtos.

    Returns:
        product (Product): Os produtos encontrados.
    """

    product = await query("SELECT ID as id, Nome, Preço, Descrição FROM produto")

    if len(product) == 0:
        return None

    dados_json = [{
    'id': item[0],
    'nome': item[1],
    'preco': str(item[2]),
    'descricao': item[3]
    } for item in product]

    json_string = json.dumps(dados_json)

    return json_string

async def update_info_product(data):
    """
    Atualiza as informações de um produto.

    Args:
        data (dict): Um dicionário com as informações do produto.

    Returns:
        product (Product): O produto atualizado.
    """

    product = await query("UPDATE produto SET Nome = %s, Preço = %s, Descrição = %s WHERE ID = %s", (data['nome'], data['preco'], data['descricao'], data['id']))

    return True

async def delete_info_product(data):
    """
    Deleta um produto.

    Args:
        data (dict): Um dicionário com as informações do produto.

    Returns:
        product (Product): O produto deletado.
    """

    product = await query("DELETE FROM produto WHERE ID = %s", (data['id']))

    return True

async def create_info_product(data):
    """
    Cria um novo produto.

    Args:
        data (dict): Um dicionário com as informações do produto.

    Returns:
        product (Product): O produto criado.
    """

    product = await query("INSERT INTO produto (Nome, Preço, Descrição) VALUES (%s, %s, %s)", (data['nome'], data['preco'], data['descricao']))

    return True
