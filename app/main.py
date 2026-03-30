from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from typing import Optional,List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schema
from .database import engine, Base
from passlib.context import CryptContext
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

pwd_context = CryptContext(schemes= ['bcrypt'], deprecated = 'auto')

Base.metadata.create_all(bind = engine) #this is when you are using the sqlalchemy db connection after base and sessionlabel
#after  that create the session object


app = FastAPI()



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


#we need a schema to ensure what is being sent is validated
#this is here pydantic comes in 
#we want a title as str, content as str, maybe category, bool, published etc

    

# try:
#     conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres',
#                              password = 'Busola123', cursor_factory= RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection successful")
# except Exception as error:
#     print("Connecting to database failed")
#     print("Error:", error)

#now we should save the posts, like a real application saves in database so we will create a makeshift data ie save in memory
#idealy each should have a unique identifier
# my_posts = [{"title": "title of post 1", "content": "content of post1", "id" : 1},
#             {"title": "favorite foods", "content": "i like pizza", "id" : 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id): #for deletion
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i #return the index 

@app.get("/")
def root():
    return {"message": "Welcome to my api"}


# @app.get("/sqlalchemy")
# def test_posts(db:Session = Depends(get_db)):
#     posts = db.query(models.Post).all() # like select all but using an orm
#     return {"status": "Success"}


