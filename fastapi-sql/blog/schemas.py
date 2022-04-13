from pydantic import BaseModel

#pydantic model
class blog_class(BaseModel):
    title : str 
    body : str 