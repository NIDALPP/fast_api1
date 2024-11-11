from pydantic import BaseModel, EmailStr
from typing import List, Optional


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str
    phone: int
    address: str


class ShowUser(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    role: str
    phone: int
    address: str

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str
    parent_category_id: Optional[int] = None
    icon: str
    active: bool = True


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    cat_id: int
    parent_category_id: Optional[int]  # make Optional

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    price: float
    cat_id: int
    brand: str
    description: str
    quantity: int
    currency: str
    image_url: str
    thumbnail: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[EmailStr] = None



class CartCreate(BaseModel):
    user_id: int
    pass


class Cart(BaseModel):
    cart_id: int
    user_id: int

    class Config:
        orm_mode = True


# class OrderProduct(BaseModel):
#     product_id: int
#     quantity: int
    
    
class OrderProduct(BaseModel):
    order_id: int
    product_id: int


class Order(BaseModel):
    order_id: int
    user_id: int
    cart_id: int
    total_amount: float
    products: List[OrderProduct]

    class Config:
        orm_mode = True
