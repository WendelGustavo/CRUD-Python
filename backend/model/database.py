from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.pool import QueuePool
import aiomysql

# Configuração do banco de dados SQLite
DATABASE_URL = 'mysql://root:@localhost/CRUD'
engine = create_engine(DATABASE_URL, poolclass=QueuePool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()

def get_db():
    """
    Função que retorna uma sessão do banco de dados.

    Returns:
        db (SessionLocal): A sessão do banco de dados.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def query(query_param, values=None):
    """
    Função que realiza uma query no banco de dados.

    Args:
        query (str): A query a ser executada.

    Returns:
        result: O resultado da query.
    """
    async with aiomysql.connect(host='localhost', user='root', password='', db='CRUD') as conn:
        async with conn.cursor() as cursor:
            # Executar a query
            if values is None:
                await cursor.execute(query_param)
                result = await cursor.fetchall()
                return result
            await cursor.execute(query_param, values)
            result = await conn.commit()
            return result
        