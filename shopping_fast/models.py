from sqlalchemy import Column,Integer,String,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Admin(Base):
    __tablename__='Admin'
    admin_id=Column(Integer,primary_key=
                    True,index=True)
    name=Column(String)
    email=Column(String(100),unique=True)
    password=Column(String(12))
    role=Column(String(100))
    
    
    
    # Admin=relationship("cust",back_populates="Admin")
    

# class Customer(Base):
#     __tablename__='Customer'
    
#     c_id=Column(Integer,primary_key=
#                     True,index=True)
#     name=Column(String)
#     email=Column(String,unique=True)
#     address=Column(String)
    

class Category(Base):
    __tablename__='Category'
    cat_id=Column(Integer,index=True)
    name=Column(String,primary_key=True,unique=True)
    
    
class Products(Base):
    __tablename__='Products'
    product_id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    price=Column(Integer)
    description=Column(String)
    stock=Column(Integer)
    cat_name=Column(Integer,ForeignKey('Category.name'))
    
    category=relationship("Category")
    