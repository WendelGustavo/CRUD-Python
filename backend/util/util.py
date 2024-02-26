from datetime import datetime, timedelta
import jwt

async def create_auth_token(user):
    """
    Cria um token de autenticação JWT para o usuário fornecido. Token é válido por 1 dia.

    Args:
        user (User): O objeto do usuário para o qual o token está sendo criado.

    Returns:
        str: O token de autenticação JWT.
    """
    payload = {
        'id': user['id'],
        'username': user['username'],
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token

def check_auth_token(token, id_user):
    """
    Verifica se o token de autenticação fornecido é válido.

    Args:
        token (str): O token de autenticação JWT. 
        id (int): O id do usuário para o qual o token está sendo verificado.

    Returns:
        bool: True se o token for válido, False caso contrário.
    """

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        if payload['id'] == id_user:
            return True
        return False
    except jwt.ExpiredSignatureError:
        return False

