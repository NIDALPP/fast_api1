from pydantic import BaseModel,EmailStr
from typing import List,Optional


class User(BaseModel):
    name:str
    email:EmailStr
    password:str
    role:str
    phone:int
    address:str
    image_url:list
class ShowUser(BaseModel):
    email:EmailStr
    password:str
    user_id:int
    role:str
    class Config():
        from_attribute=True
    
class CategoryBase(BaseModel):
    name: str
    parent_category_id:Optional[int]=None
    active:bool=True
    icon:list
class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    cat_id:int
    parent_category_id:int
    class Config:
        from_attribute = True
    
    
class productBase(BaseModel):
    name:str
    price:float
    cat_id:int
    brand:str
    description:str
    quantity:int
    currency:str
    image_url:list
    thumbnail:list
    
class ProductCreate(productBase):
    pass

class Product(productBase):
    product_id:int
    category:Optional[str]=None
    class config:
        from_attribute=True
    
    
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[EmailStr] = None
    
    
class cartBase(BaseModel):
    product_id:int
    quantity:int
    
class cartCreate(cartBase):

    pass

class cart(cartBase):
    # user_id:int
    cart_id:int
    class Config:
        from_attribute = True 