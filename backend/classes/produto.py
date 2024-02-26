from sqlalchemy import Column, Integer, String
from model.productModel import get_info_product, update_info_product, delete_info_product, create_info_product


class Product:
    """
    Classe que representa a tabela de produto no banco de dados.

    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)


    async def get_product(self, table):
        """
        Rota responsável por retornar todos os produtos.

        Returns:
            products (list): A lista de produtos.
        """

        products = await get_info_product()

        if (products is None):
            return {'message': 'Nenhum produto encontrado!', 'status': False}
        return {'message': 'Produtos encontrados!', 'products': products, 'status': True}
    
    async def update_product(self, data):
        """
        Rota responsável por atualizar um produto.

        Returns:
            message (str): A mensagem de sucesso ou falha da atualização do produto.
        """

        updated_product = await update_info_product(data)

        print(updated_product)

        if (updated_product is None):
            return {'message': 'Produto não encontrado!', 'status': False}
        return {'message': 'Produto atualizado!', 'status': True}
    
    async def delete_product(self, data):
        """
        Rota responsável por deletar um produto.

        Returns:
            message (str): A mensagem de sucesso ou falha da deleção do produto.
        """

        deleted_product = await delete_info_product(data)

        if (deleted_product is None):
            return {'message': 'Produto não encontrado!', 'status': False}
        return {'message': 'Produto deletado!', 'status': True}
    
    async def create_product(self, data):
        """
        Rota responsável por criar um produto.

        Returns:
            message (str): A mensagem de sucesso ou falha da criação do produto.
        """

        created_product = await create_info_product(data)

        if (created_product is None):
            return {'message': 'Produto não encontrado!', 'status': False}
        return {'message': 'Produto criado!', 'status': True}
    
    
        
    
    

        

        




    


    