from model.database import query

async def get_info_user_by_email(email):
    """
    Retorna as informações do usuário pelo email.

    Args:
        email (str): O email do usuário.

    Returns:
        user (User): O usuário encontrado.
    """

    user = await query(f"SELECT id_user as id, username, email, password FROM User WHERE email = '{email}'")

    if len(user) == 0:
        return None

    return user[0]

async def create_user(username, password, email):
    """
    Cria um novo usuário no banco de dados.

    Args:
        username (str): O nome de usuário.
        password (str): A senha do usuário.
        email (str): O email do usuário.

    Returns:
        message (str): Mensagem de sucesso do cadastro.
    """

    query_insert = "INSERT INTO User (username, password, email) VALUES (%s, %s, %s)"

    result = await query(query_insert, (username, password, email))
    
    return result


