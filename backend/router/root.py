from flask import Blueprint, send_from_directory, jsonify
import os

# Criar um Blueprint para o roteador
router = Blueprint('router', __name__)

# Configurando o caminho para o diretório frontend
frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'frontend')


# Rota para servir o arquivo index.html
@router.route('/')
def index():
    """
    Retorna a página inicial da aplicação.

    Returns:
        file: O arquivo index.html.

    """
    return send_from_directory(frontend_dir, 'index.html')

# Rota para a página "about"
@router.route('/about/info')
def get_about():
    """
    Retorna informações referentes a versão e descrição da aplicação. Utilizada para controle de versão e documentação.

    Returns:
        name (str): O nome da aplicação.
        version (str): A versão da aplicação.
        description (str): A descrição da aplicação.
        license (str): A licença da aplicação.
        repository (str): O repositório da aplicação.


    """

    return jsonify({ "name": "CRUD - Aplicação web simples utilizando Python com o framework Flask",
                    "version": "1.0.0", 
                    "Description": "Aplicação web simples utilizando Python com o framework Flask, que permite aos usuários criar, visualizar, editar e deletar registros de uma entidade específica em um banco de dados MySQL. A aplicação também deve ter uma interface básica utilizando HTML/CSS." ,
                    "License": "https://github.com/WendelGustavo/CRUD-Python/blob/main/LICENSE",
                    "repository": "https://github.com/WendelGustavo/CRUD-Python",
                    }), 200