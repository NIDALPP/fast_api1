from sqlalchemy import Column,Integer,String,ForeignKey,Boolean,URL
from .database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__='user'
    user_id=Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True)
    email=Column(String,unique=True)
    password=Column(String)
    role=Column(String)
    phone=Column(Integer,unique=True)
    address=Column(String)
    image_url=Column(String)

    carts = relationship("Cart", back_populates="user")


class Category(Base):
    __tablename__='Category'
    cat_id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String,unique=True)
    active=Column(Boolean)
    icon=Column(String)
    parent_category_id=Column(Integer, ForeignKey('Category.cat_id'), nullable=True)    
    parent_category = relationship("Category", remote_side=[cat_id])
    
class Products(Base):
    __tablename__='Products'
    product_id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    price=Column(Integer)
    currency=Column(String)
    brand=Column(String)
    description=Column(String)
    quantity=Column(Integer)
    image_url=Column(String)
    cat_id=Column(Integer,ForeignKey('Category.cat_id'))
    thumbnail=Column(String)
    
    category=relationship("Category")
    
    
class Cart(Base):
    __tablename__='cart'
    cart_id=Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))  
    product_id=Column(Integer,ForeignKey('Products.product_id'))
    quantity=Column(Integer)
    
    user = relationship("User", back_populates="carts")  
    products = relationship("Products")
    
# class orders(Base):
#     __tablename__='orders'
#     order_id=Column(Integer,primary_key=True,index=True)
#     user_id=Column(Integer,ForeignKey('user.user_id'))
#     address=Column(String,ForeignKey('User.address'))
    
    
#     user=relationship("User")