from pydantic import BaseModel
from typing import List,Optional

class Admin(BaseModel):
    name:str
    admin_id:int
    email:str
    password:str
    role:str
    
    
class ShowAdmin(BaseModel):
    admin_id:int
    name:str
    email:str
    role:str
    class Config():
        from_attribute=True
    
    
class CategoryBase(BaseModel):
    name: str
    
    

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    cat_id: int

    class Config:
        from_attribute = True
    
    
class productBase(BaseModel):
    name:str
    price:float
    cat_name:str
    stock:int
    description:Optional[str]=None
    
class ProductCreate(productBase):
    pass

class Product(productBase):
    name:str
    product_id:int
    category:Optional[Category]=None
    class config:
        from_attribute=True
    
    