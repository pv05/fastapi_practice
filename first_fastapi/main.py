from genericpath import exists
from fastapi import FastAPI

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


