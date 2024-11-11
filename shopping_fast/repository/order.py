from sqlalchemy.orm import Session
from typing import Optional
from . .import models

class cart_create:
    def __init__(self, db: Session):
        self.db = db

    def get_product_by_id(self, product_id: int) -> Optional[models.Product]:
        return self.db.query(models.Product).filter(models.Product.product_id == product_id).first()

    def get_cart_by_user_id(self, user_id: int) -> Optional[models.Cart]:
        return self.db.query(models.Cart).filter(models.Cart.user_id == user_id).first()

    def get_cart_item(self, cart_id: int, product_id: int) -> Optional[models.CartItem]:
        return self.db.query(models.CartItem).filter(
            models.CartItem.cart_id == cart_id, 
            models.CartItem.product_id == product_id
        ).first()

    def add_product_to_cart(self, cart_id: int, product_id: int, quantity: int) -> models.CartItem:
        cart_item = models.CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
        self.db.add(cart_item)
        self.db.commit()
        self.db.refresh(cart_item)
        return cart_item

    def update_cart_item(self, cart_item: models.CartItem, quantity: int) -> models.CartItem:
        cart_item.quantity += quantity
        self.db.commit()
        self.db.refresh(cart_item)
        return cart_item
