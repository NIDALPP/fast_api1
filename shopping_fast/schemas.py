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
        from_attributes = True


class CategoryBase(BaseModel):
    name: str
    parent_category_id: Optional[int] = None
    icon: str
    active: bool = True


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    cat_id: int
    parent_category_id: Optional[int] 

    class Config:
        from_attributes = True


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
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id:Optional[int]=None
    email: Optional[EmailStr] = None



class CartCreate(BaseModel):
    user_id: int
    pass


class Cart(BaseModel):
    cart_id: int
    user_id: int

    class Config:
        from_attributes = True

class CartItemCreate(BaseModel):
    product_id: int
    
    quantity: int

class CartItemUpdate(BaseModel):
    quantity: int

class ProductInCartItem(BaseModel):
    product_id: int
    name: str
    price: float
    currency: str

    class Config:
        from_attributes = True



class CartItem(BaseModel):
    cart_item_id: int
    cart_id: int
    user_id: int
    product: ProductInCartItem
    quantity: int

    class Config:
        from_attributes = True

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    total_amount:float

    class Config:
        from_attributes = True


class Order(BaseModel):
    order_id: int
    user_id: int
    cart_id: int
    total_amount: float
    class Config:
        from_attributes = True
