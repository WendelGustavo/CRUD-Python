from flask import Flask, request, send_from_directory
from middleware.authMiddleware import auth_middleware
from router.root import router
from router.product import product
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

@app.route('/register')
def register():
    """
    Rota para a página de cadastro.

    Returns:
        register.html: A página de cadastro.
    
    """
    return send_from_directory(frontend_dir, 'register/index.html')

@app.route('/home')
def home():
    """
    Rota para a página home.

    Returns:
        home.html: A página home.
    
    """
    return send_from_directory(frontend_dir, 'home/index.html')

@app.route('/about')
def about():
    """
    Rota para a página sobre.

    Returns:
        about.html: A página sobre.
    
    """
    return send_from_directory(frontend_dir, 'about/index.html')


# Registrando as rotas
app.register_blueprint(router)
app.register_blueprint(user)
app.register_blueprint(product)


if __name__ == '__main__':
    app.run(debug=True)
