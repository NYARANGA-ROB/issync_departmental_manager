from prisma import Prisma
from contextlib import asynccontextmanager
from fastapi import FastAPI

prisma = Prisma()

@asynccontextmanager
async def connect_to_databse(app: FastAPI):
    await prisma.connect()
    yield
    await prisma.disconnect()
