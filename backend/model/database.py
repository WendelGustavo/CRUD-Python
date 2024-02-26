import aiomysql

async def query(query_param, values=None):
    """
    Função que realiza uma query no banco de dados.

    Args:
        query (str): A query a ser executada.

    Returns:
        result: O resultado da query.
    """
    async with aiomysql.connect(host='', user='', password='', db='') as conn:
        async with conn.cursor() as cursor:
            # Executar a query
            if values is None:
                await cursor.execute(query_param)
                result = await cursor.fetchall()
                return result
            await cursor.execute(query_param, values)
            result = await conn.commit()
            return result
        