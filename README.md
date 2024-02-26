# Teste prático - 

Neste repositório criei o front-end/back-end de uma página de gerencimaneto de clientes.

## 📖 Sobre o projeto

Aplicação web simples utilizando Python com o framework Flask, que permite aos usuários criar, visualizar, editar e deletar registros de uma entidade específica em um banco de dados MySQL. A aplicação também deve ter uma interface básica utilizando HTML/CSS.

Neste teste, foi implementado as seguintes funcionalidades de acordo com os requisitos:

### Funcionalidades
- Exibição de todos os clientes cadastrados.
- Opção de filtrar clientes com base nas informações de nome, email e telefone.
- Possibilidade de adicionar novos clientes à plataforma.
- Implementação de algoritmo para calcular a rota mais eficiente.
- Utilização de coordenadas bidimensionais (X, Y) para representar a localização dos clientes.

## ⚙️ Como executar o front-end

Para executar a aplicação localmente, siga os passos abaixo:

1. Clone este repositório:

```bash
  https://github.com/vinikrummenauer/sistema_clientes.git
  cd sistema_clientes
```

2. Instale as dependências na pasta frontend:

```bash
  npm install
```

3. Iniciar a aplicação no frontend:

```bash
  npm run dev
```

## ⚙️ Como executar o back-end

Você precisará ter o PostgreeSQL instalado na sua máquina.

1. Crie um banco de dados no MySQL:

```bash
  Crie um banco de dados Postgree e guarde as seguintes informações: host, porta, database, user e a senha.
  Vá até a pasta db e configure o arquivo config.js de acordo com as informações guardadas acima.
```

2. Crie as tabelas e insira os dados:

```bash
  Na pasta db copie o script do arquivo "db.sql" e execute o script no seu banco de dados recém criado.
```

4. Instale as dependências na pasta backend:
```bash
  npm install
```

5. Inicie a aplicação
```bash
  npm start
```
