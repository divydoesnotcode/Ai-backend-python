# This holds all the data 

from pydantic import BaseModel

class Product(BaseModel):
    id:int 
    name:str
    price:float
    quantity:int
