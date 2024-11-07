from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status


def create(request: schemas.cartCreate,db: Session):
    new_cart = models.Cart(product_id=request.product_id,quantity=request.quantity)
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart
