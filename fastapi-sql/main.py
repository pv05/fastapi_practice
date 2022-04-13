from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/home") # that's called decorator
def index():
    # return "hello, i am pankaj"
    return {'data':{'name':'pankaj'}} # this is return like a json struture


@app.get('/blog/public')
def blog_public(limit=90,public:bool=True):
    
    if public:
        return {'data':f"{limit} blogs from database is public"}
    else:
        return {'data':f"{limit} blog from database"}

@app.get('/blog/{id}')
def show(id:int): # id should be integer by default it string
    return {'data':id}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished data'}



#pydantic use
class Blog_class(BaseModel):
    title: str 
    body: str
    published: Optional[bool]


# use post method
@app.post('/blog')
def create_blog(blog:Blog_class):
    # return request
    return {'data':f'blog title is {blog.title}'}

