from sqlalchemy.orm import Session
from typing import Optional, List
from . .import models

class CartCreate:
    def __init__(self, db: Session):
        self.db = db

    def get_product_by_id(self, product_id: int) -> Optional[models.Product]:
        return self.db.query(models.Product).filter(models.Product.product_id == product_id).first()

    def get_cart_by_user_id(self, user_id: int) -> Optional[models.Cart]:
        return self.db.query(models.Cart).filter(models.Cart.user_id == user_id).first()

    def get_cart_item(self,cart_item_id: int, cart_id: int,user_id: int, product_id: int=None ) -> Optional[models.CartItem]:
        return self.db.query(models.CartItem).filter(
            models.CartItem.cart_id == cart_id, 
            models.CartItem.product_id == product_id,
            models.CartItem.user_id == user_id,
            models.CartItem.cart_item_id == cart_item_id
            

        ).first()

    def add_product_to_cart(self, cart_id: int, product_id: int, quantity: int, user_id: int) -> models.CartItem:
        cart_item = models.CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity, user_id=user_id,)
        self.db.add(cart_item)
        self.db.commit()
        self.db.refresh(cart_item)
        return cart_item

    def update_cart_item(self, cart_item: models.CartItem, quantity: int) -> models.CartItem:
        cart_item.quantity += quantity
        self.db.commit()
        self.db.refresh(cart_item)
        return cart_item

    def get_all_cart_items(self, cart_id: int,user_id:int) -> List[models.CartItem]:
        cart=self.db.query(models.CartItem).filter(
            models.CartItem.cart_id == cart_id, 
            models.CartItem.user_id == user_id
        ).all()
        return cart

    def clear_cart(self, cart_id: int) -> None:
        self.db.query(models.CartItem).filter(models.CartItem.cart_id == cart_id).delete()
        self.db.commit()