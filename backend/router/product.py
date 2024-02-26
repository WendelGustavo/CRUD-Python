from flask import Blueprint, jsonify, request
from classes.produto import Product


# Criar um Blueprint para o roteador
product = Blueprint('product', __name__)

@product.route('/products', methods=['GET'])
async def get_products():
    """
       Rota responsável por retornar todos os produtos.

        Returns:
            products (list): A lista de produtos.
    """
    product_class = Product()
    products = await product_class.get_product('products')

    if not products['status']:
        return jsonify({'message': products['message'], 'status': products['status']}), 404
    return jsonify({'message': products['message'], 'products': products['products'], 'status': products['status']}), 200

@product.route('/product', methods=['PUT'])
async def update_product():
    """
    Rota responsável por atualizar um produto.

    Returns:
        message (str): A mensagem de sucesso ou falha da atualização do produto.
    """
    data = request.json
    product_class = Product()
    response = await product_class.update_product(data)

    if not response['status']:
        return jsonify({'message': response['message'], 'status': response['status']}), 404
    return jsonify({'message': response['message'], 'status': response['status']}), 200

@product.route('/product', methods=['DELETE'])
async def delete_product():
    """
    Rota responsável por deletar um produto.

    Returns:
        message (str): A mensagem de sucesso ou falha da deleção do produto.
    """
    data = request.json
    product_class = Product()
    response = await product_class.delete_product(data)

    if not response['status']:
        return jsonify({'message': response['message'], 'status': response['status']}), 404
    return jsonify({'message': response['message'], 'status': response['status']}), 200

@product.route('/product', methods=['POST'])
async def create_product():
    """
    Rota responsável por criar um produto.

    Returns:
        message (str): A mensagem de sucesso ou falha da criação do produto.
    """
    data = request.json
    product_class = Product()
    response = await product_class.create_product(data)

    if not response['status']:
        return jsonify({'message': response['message'], 'status': response['status']}), 404
    return jsonify({'message': response['message'], 'status': response['status']}), 200





