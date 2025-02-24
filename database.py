from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# MongoDB connection
DATABASE_URL = os.getenv("DATABASE_URL")
client = AsyncIOMotorClient(DATABASE_URL)
engine = AIOEngine(client=client, database="sgaa")

def get_engine() -> AIOEngine:
    return engine