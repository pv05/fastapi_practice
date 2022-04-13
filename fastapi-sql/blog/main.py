from turtle import title
from fastapi import FastAPI,Depends
from . import schemas,models # schemas.py file import from same directory
from . database import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine) # this line is create the table in blog.db

# step:1/2 blog add in databse
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

# step:2/2 - blog add in databse
@app.post('/blog',status_code=201) # status_code must be 201 which indicates that the request has succeeded and new resources has been created
def create(request:schemas.blog_class, db:Session=Depends(get_db)): # Depends convert session into pydantic
    new_blog = models.Blog(title = request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog    

# step:1/1 - getting blog from database
@app.get('/blog')
def all_blogs(db: Session = Depends(get_db)): # datasbe instant
    blogs = db.query(models.Blog).all() # show the all rows which present in databse
    return blogs

# step:1/1 - getting a blog by ID number from databse
@app.get('/blog/{id}')
def blog_by_id(id, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first() # using first() it show in this form -->{..} or using all() it show in this form --> [{..}]
    return blogs

