from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float, Table
from sqlalchemy.orm import relationship
from .database import Base

order_products = Table(
    'order_products', Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.order_id')),
    Column('product_id', Integer, ForeignKey('products.product_id'))
)

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    phone = Column(Integer, unique=True)
    address = Column(String)
    image_url = Column(String)
    cart = relationship("Cart", uselist=False, back_populates="user")
    orders = relationship("Order", back_populates="user")
    
    cart_items = relationship("CartItem", back_populates="user")
    
    orders = relationship("Order", back_populates="user", foreign_keys="[Order.user_id]")

class Category(Base):
    __tablename__ = 'categories'
    cat_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True)
    active = Column(Boolean)
    icon = Column(String)
    parent_category_id = Column(Integer, ForeignKey('categories.cat_id'), nullable=True)
    
    parent_category = relationship("Category", remote_side=[cat_id], back_populates="sub_categories")
    sub_categories = relationship("Category", back_populates="parent_category")  # For child categories
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    currency = Column(String)
    brand = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    image_url = Column(String)
    thumbnail = Column(String)
    cat_id = Column(Integer, ForeignKey('categories.cat_id'))

    category = relationship("Category", back_populates="products")
    cart_items = relationship("CartItem", back_populates="product")
    orders = relationship("Order", secondary=order_products, back_populates="products")


class Cart(Base):
    __tablename__ = 'carts' 
    cart_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), unique=True)

    user = relationship("User", back_populates="cart")
    orders = relationship("Order", back_populates="cart")
    cart_items = relationship("CartItem", back_populates="cart")  

class CartItem(Base):
    __tablename__ = 'cart_items'
    
    cart_item_id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('carts.cart_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    order_id = Column(Integer, ForeignKey('orders.order_id')) 
    
    cart = relationship("Cart", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")
    user = relationship("User", back_populates="cart_items")
    order = relationship("Order", back_populates="cart_items")  



class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    cart_id = Column(Integer, ForeignKey("carts.cart_id"), nullable=False)
    total_amount = Column(Float, nullable=False)
    address = Column(String, nullable=False)
    user = relationship("User", back_populates="orders")
    cart = relationship("Cart", back_populates="orders")
    cart_items = relationship("CartItem", back_populates="order") 
    products = relationship("Product", secondary=order_products, back_populates="orders")
