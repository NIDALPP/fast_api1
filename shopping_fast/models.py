from sqlalchemy import Column,Integer,String,ForeignKey,Boolean,Enum
from .database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__='user'
    admin_id=Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True)
    email=Column(String,unique=True)
    password=Column(String)
    role=Column(String)
    phone=Column(Integer,unique=True)
    address=Column(String)
    image_url=Column(String)


class Category(Base):
    __tablename__='Category'
    cat_id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String,unique=True)
    active=Column(Boolean)
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
    cat_id=Column(Integer,ForeignKey('Category.cat_id'))
    
    category=relationship("Category")
    