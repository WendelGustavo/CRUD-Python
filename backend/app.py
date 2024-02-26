from flask import Flask, request, send_from_directory
from middleware.authMiddleware import auth_middleware
from router.root import router
from router.user import user
from flask_cors import CORS

app = Flask(__name__)

CORS(app, supports_credentials=True)

# Middleware
@app.before_request
def my_middleware():

    """
    Middleware para verificar se o token de autenticação fornecido é válido.

    Args:
        request (Request): O objeto de requisição.

    Returns:
        Response: A resposta de sucesso ou falha da verificação do token.

    """
    print(request.path)
    if request.path == '/' or request.path == '/about' or request.path == '/login' or request.path == '/register':
        return
    else:
        auth_middleware(request)

# Diretório do frontend
frontend_dir = '../frontend/pages/'

@app.route('/')
def index():
    """
    Rota para a página inicial.

    Returns:
        index.html: A página inicial.
    
    """
    return send_from_directory(frontend_dir, 'login/index.html')

@app.route('/about')
def about():
    """
    Rota para a página sobre.

    Returns:
        about.html: A página sobre.
    
    """
    return send_from_directory(frontend_dir, 'about.html')

@app.route('/register')
def register():
    """
    Rota para a página de cadastro.

    Returns:
        register.html: A página de cadastro.
    
    """
    return send_from_directory(frontend_dir, 'register.html')


# Registrando as rotas
app.register_blueprint(router)
app.register_blueprint(user)

if __name__ == '__main__':
    app.run(debug=True)
