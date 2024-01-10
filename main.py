from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime
from starlette.responses import JSONResponse
from api.author import authorRouter
from api.books import bookRouter
from models.db_models import Author
from db import create_tables, get_session, db_init

create_tables()
db_init()

app = FastAPI()
app.include_router(bookRouter)
app.include_router(authorRouter)

# занесение информации о включении и выключении в log.txt
@app.on_event("startup")
def startup():
    open("log.txt", mode="a").write(f'{datetime.utcnow()}: Begin\n')


@app.on_event("shutdown")
def shutdown():
    open("log.txt", mode="a").write(f'{datetime.utcnow()}: End\n')


@app.get('/')
def index():
    db_init()
    return "Hello"
