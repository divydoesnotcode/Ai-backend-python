from fastapi import FastAPI      # Core Framework
from models import Product      # Importing product model
# from pydantic import BaseModel   # Basemodel helps in validation
# from typing import List          # For type hinting

app = FastAPI()                # Create FastAPI instance

# Decorator used to give power to the function

@app.get("/")
def read_root():
    return {"Message": "Welcome to the My Tea API"}

products = [
    Product(id=1, name="Green Tea", price=10.99, quantity=100),
    Product(id=2, name="Black Tea", price=8.99, quantity=150),
    Product(id=3, name="Oolong Tea", price=12.99, quantity=80),
    Product(id=4, name="White Tea", price=15.99, quantity=60),
    Product(id=5, name="Herbal Tea", price=9.99, quantity=200)
]

@app.get("/products")
def getProducts():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "Product not found"

@app.get("/products/")
def get_all_products():
    return products