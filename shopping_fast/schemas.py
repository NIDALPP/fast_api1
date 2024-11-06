from pydantic import BaseModel,EmailStr
from typing import List,Optional


class User(BaseModel):
    name:str
    email:EmailStr
    password:str
    role:str
    phone:int
    address:str
    
    
class ShowUser(BaseModel):
    admin_id:int
    name:str
    email:EmailStr
    role:str
    phone:int
    address:str
    class Config():
        from_attribute=True
    
class CategoryBase(BaseModel):
    name: str
    parent_category_id:Optional[int]=None
    active:bool=True
class CategoryCreate(CategoryBase):
    
    pass

class Category(CategoryBase):
    cat_id:int
    class Config:
        from_attribute = True
    
    
class productBase(BaseModel):
    name:str
    price:float
    cat_id:str
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
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[EmailStr] = None