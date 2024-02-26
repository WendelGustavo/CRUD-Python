from flask import jsonify
from util.util import check_auth_token

def auth_middleware(request):
    """
    Middleware para verificar se o token de autenticação fornecido é válido.

    Args:
        request (Request): O objeto de requisição.

    Returns:
        Response: A resposta de sucesso ou falha da verificação do token.
    """
    if not request.is_json:
        return jsonify({'message': 'O corpo da requisição não é um JSON!'}), 400
    if request.headers.get('Authorization') is None or request.headers.get('idUser') is None:
        return jsonify({'message': 'Credenciais de autenticação não fornecidas'}), 401
    # Verifica se o token de autenticação fornecido é válido
    if not check_auth_token(
        request.headers.get('Authorization'),
        request.headers.get('idUser')
    ):
        return jsonify({'message': 'Token de autenticação inválido'}), 401
    return jsonify({'message': 'Token de autenticação válido'}), 200
