import asyncio, os
from sqlalchemy.ext.asyncio import create_async_engine

url = os.getenv("DATABASE_URL")
if not url:
    print("DATABASE_URL não definido")
    raise SystemExit(1)

engine = create_async_engine(url, connect_args={"sslmode":"require"})

async def main():
    async with engine.connect() as conn:
        version = (await conn.exec_driver_sql("select version()")).scalar()
        dbname = (await conn.exec_driver_sql("select current_database()")).scalar()
        print("OK:", dbname)
        print(version)

asyncio.run(main())
