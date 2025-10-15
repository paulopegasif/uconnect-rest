import asyncio, asyncpg, ssl, pathlib

ssl_ctx = ssl.create_default_context(
    cafile=str(pathlib.Path(__file__).resolve().parent / "app" / "certs" / "ca.pem")
)

async def test():
    conn = await asyncpg.connect(
        user="avnadmin",
        password="AVNS_ZNdJaYqcEhNaEf1dsCl",
        database="defaultdb",
        host="uconnect-uconnect.c.aivencloud.com",
        port=24757,
        ssl=ssl_ctx,
    )
    print("Conectado com sucesso!")
    await conn.close()

asyncio.run(test())