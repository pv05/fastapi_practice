from turtle import title
from . database import Base # Base fucntion from database.py
from sqlalchemy import Column,Integer,String

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    
