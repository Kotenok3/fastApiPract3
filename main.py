from fastapi import FastAPI
from datetime import datetime
from api.author import authorRouter
from api.books import bookRouter
from db import create_tables, db_init

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
