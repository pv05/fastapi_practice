from importlib.metadata import metadata
from fastapi import FastAPI
from . import schemas,models # schemas.py file import from same directory
from . database import engine

app = FastAPI()

models.Base.metadata.create_all(engine) # this line is create the table in blog.db

@app.post('/blog')
def create(blog:schemas.blog_class):
    return {'title':blog.title,'body':blog.body}