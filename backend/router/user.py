from flask import Blueprint, jsonify, request
from classes.user import User
import asyncio


# Criar um Blueprint para o roteador
user = Blueprint('user', __name__)


# Rota responsável pelo login do usuário
@user.route('/login', methods=['POST'])
async def login_user():
    """
       Rota responsável pela autenticação do usuário.

        Args:
            username (str): O nome de usuário.
            password (str): A senha do usuário.

       Returns:
            Token (str): O token de autenticação JWT.
            message (str): Mensagem de sucesso da autenticação.
            id (int): O id do usuário autenticado.
    """

    data = request.json

    if data.get('email') is None or data.get('password') is None:
        return jsonify({'message': 'Credenciais de autenticação não fornecidas!'}), 401

    email = data.get('email')
    password = data.get('password')

    user_class = User()

    respost = await user_class.login_user(email, password)

    if not respost['status']:
        return jsonify({'message': respost['message'], 'status': respost['status']}), 401
    token = respost['token']
    id_user = respost['id']

    return jsonify({'token': token, 'message': 'Usuário autenticado com sucesso!', 'id': id_user, 'status': True})

# Rota responsável pelo cadastro do usuário
@user.route('/register', methods=['POST'])
async def register_user():
    """
       Rota responsável pelo cadastro do usuário.

        Args:
            username (str): O nome de usuário.
            password (str): A senha do usuário.
            email (str): O email do usuário.

       Returns:
            message (str): Mensagem de sucesso do cadastro.
    """

    data = request.json

    if (data.get('username') is None or data.get('password') is None or data.get('email') is None):
        return {'message': 'Credenciais de autenticação não fornecidas!', 'status': False}

    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    user_class = User()

    respost = await user_class.create_user(username, password, email)

    if not respost['status']:
        return jsonify({'message': respost['message'], 'status': False}), 401
    return jsonify({'message': 'Usuário cadastrado com sucesso!', 'status': True, 'id': respost['id'], 'token': respost['token']})
