# Teste prático -  S4 SMART SUPPLY

CRUD simples, utilizando Python com o FrameWork Flask.

## 📖 Sobre o projeto

Aplicação web simples utilizando Python com o framework Flask, que permite aos usuários criar, visualizar, editar e deletar registros de uma entidade específica em um banco de dados MySQL. A aplicação também deve ter uma interface básica utilizando HTML/CSS.

Neste teste, foi implementado as seguintes funcionalidades de acordo com os requisitos:

### Funcionalidades
- [x] Exibição de todos os produtos cadastrados.
- [x] Opção de editar, remover e adicionar novos Produtos.
- [x] Implementação de sistema de autenticação do usuario com JWT
- [x] Middleware responsável por garantir veracidade das informações enviadas pelos usuários.

### Estrutura Base do projeto

```
/backend               -> Pasta contendo o código do lado do servidor.
    |__classes         -> Pasta contendo as Classes necessarias do backend.
    |__middleware      -> Middleware para processamento intermediário das requisições e vaidação de usuário.
    |__model           -> Pasta contendo configuração e comunicação com o banco de dados.
    |__router          -> Roteadores para direcionar solicitações.
    |__util            -> Pasta contendo utilitários diversos.
    app.py             -> Arquivo principal de inicialização do servidor.

/frontend              -> Pasta contendo o código do lado do cliente.
    |__pages           -> Páginas HTML.
    |__styles          -> Estilos CSS.
    
requirements.txt       -> Arquivo que carrega as dependências necessárias do projeto.
```


## ⚙️ Como executar o projeto

Para executar a aplicação localmente, siga os passos abaixo:

1. Clone este repositório:

```
  git clone https://github.com/WendelGustavo/CRUD-Python
```

1.1  Instale as dependencias base
```
  pip install -r requirements.txt
```

1.2 Acesse a pasta Backend
```
  cd backend
```
2. Crie um banco de dados no MySQL:

```
  Crie um banco de dados SQL e guarde as seguintes informações: host, porta, database, user e a senha.
  Vá até a pasta backend/model e configure o arquivo database.py de acordo com as informações guardadas acima.
  Informações ncessárias: 
  host= Host do seu Banco de Dados
  user= Username do seu Usuário de Banco de Dados
  password= Senha do seu Usuário de Banco de Dados
  db= Nome do Banco de dados Criado
```

3. Crie as tabelas e insira os dados:
```
  Ainda na pasta model copie o script do arquivo "db.txt" e execute o script no seu banco de dados recém criado.
```

5. Inicie a aplicação
```
  python app.py
```
6. Abra a aplicação no host inforamado no terminal

## 🎥 Vídeo demonstrativo das funcionalidades 
  [Vídeo](https://drive.google.com/file/d/12ER1bniYG3GI6bxhik7fY8o1Pj1vF9Hg/view?usp=sharing)

## 📖 Licença

Esse projeto está sob a licença (nome da licença) - acesse os detalhes [LICENSE.md](https://github.com/WendelGustavo/CRUD-Python/blob/main/LICENSE).



