from fastapi import FastAPI

app = FastAPI()

@app.get("/home") # that's called decorator
def index():
    return "hello, i am pankaj"
    # return {'data':{'name':'pankaj'}} # this is return like a json struture
