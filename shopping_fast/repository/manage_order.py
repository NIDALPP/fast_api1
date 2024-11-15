from sqlalchemy.orm import Session,joinedload
from .. import models, schemas
from typing import List

class OrderCreate:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, user_id: int, cart_id: int,address:str) -> models.Order:
        cart_items = self.db.query(models.CartItem).filter(
            models.CartItem.cart_id == cart_id
        ).all() 

        if not cart_items:
            raise ValueError("Cart is empty or cart items could not be found")

        total_amount = sum(item.quantity * item.product.price for item in cart_items)

        if user_id is None or cart_id is None:
            raise ValueError("User ID and Cart ID cannot be None")

        order = models.Order(user_id=user_id, cart_id=cart_id, total_amount=total_amount,address=address)
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        
        return order
def get_all(db: Session) -> List[models.Order]:
    orders = db.query(models.Order).options(joinedload(models.Order.cart_items)).all()
    return orders