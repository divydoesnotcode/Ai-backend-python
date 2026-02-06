# This holds all the data 
from sqlalchemy import Column, Integer, String
from database import Base

# from pydantic import BaseModel

# class Product(BaseModel):
#     id:int 
#     name:str
#     price:float
#     quantity:int

class Vendor(Base):
    __tablename__ = "Vendors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)
    contact = Column(String)

