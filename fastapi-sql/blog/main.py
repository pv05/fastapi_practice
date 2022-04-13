from fastapi import FastAPI,Depends,Response,status,HTTPException
from . import schemas,models # schemas.py file import from same directory
from . database import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine) # this line is create the table in blog.db

''' We going to Apply CRUD Operation'''

# step:1/2 CREATE blog in database
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

# step:2/2 - CREATE blog in databse
@app.post('/blog',status_code=201) # status_code must be 201 which indicates that the request has succeeded and new resources has been created
def create(request:schemas.blog_class, db:Session=Depends(get_db)): # Depends convert session into pydantic
    new_blog = models.Blog(title = request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog    

# step:1/1 - READ blog or getting blog from database
@app.get('/blog')
def all_blogs(db: Session = Depends(get_db)): # datasbe instant
    blogs = db.query(models.Blog).all() # show the all rows which present in databse
    return blogs

# step:1/1 - READ blog or getting a blog by ID number from databse
@app.get('/blog/{id}')
def blog_by_id(id,response:Response ,db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first() # using first() it show in this form -->{..} or using all() it show in this form --> [{..}]
    if not blogs:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail":f"id={id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id={id} not found!!") # this single code is alternatie of above two line code
    return blogs

# step:1/1 - DELTE the blog
@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id) # blog deleted by ID
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id={id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "delete success"

# step:1/1 - UPDATE the blog    
@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request:schemas.blog_class ,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id={id} not found")
    blog.update(request.dict())
    db.commit()
    return "update success"

