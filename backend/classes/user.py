from sqlalchemy import Column, Integer, String
from model.userModel import get_info_user_by_email, create_user
from util.util import create_auth_token


class User:
    """
    Classe que representa a tabela de usuários no banco de dados.

    Args:
        Base (Base): A classe base do SQLAlchemy.

    """


    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)



    async def login_user(self, email, password):
        """
        Cria um novo usuário no banco de dados.

        Args:
            password (str): A senha do usuário.
            email (str): O email do usuário.

        Returns:
            message (str): Mensagem de sucesso da autenticação.
            id (int): O id do usuário autenticado.
            token (str): O token de autenticação JWT.
            status (bool): Status da autenticação.
        """

        response = await get_info_user_by_email(email)


        if response is None:
            return {'message': 'Usuário não encontrado!', 'status': False}
        if response[3] != password:
            return {'message': 'Senha incorreta!', 'status': False}

        response = {
        'id': response[0],
        'username': response[1],
        'email': response[2],
        'password': response[3]
        }

        token = await create_auth_token(response)
        return {'message': 'Usuário autenticado com sucesso!', 'id': response['id'], 'token': token, 'status': True }

    async def create_user(self, username, password, email):

        """
        Cria um novo usuário no banco de dados.

        Args:
            username (str): O nome de usuário.
            password (str): A senha do usuário.
            email (str): O email do usuário.

        Returns:
            message (str): Mensagem de sucesso do cadastro.
            status (bool): Status do cadastro.
        """


        get_user = await get_info_user_by_email(email)

        if get_user is not None:
            return {'message': 'Email já cadastrado!', 'status': False}
        response = await create_user(username, password, email)


        get_user = await get_info_user_by_email(email)

        if get_user is None:
            return {'message': 'Erro ao cadastrar usuário!', 'status': False}
        
        response = {
            'id': get_user[0],
            'username': get_user[1],
            'email': get_user[2],
            'password': get_user[3]
        }
        
    
        token = await create_auth_token(response)
        return {'message': 'Usuário cadastrado com sucesso!', 'status': True, 'id': response['id'], 'token': token}
