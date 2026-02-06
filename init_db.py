import asyncio 
from database import Base, engine
import models

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init())

# To run this file, use the command: python init_db.py
# This will create the database tables based on the models defined in models.py