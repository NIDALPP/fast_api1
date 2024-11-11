from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status





def get_all(db: Session):
    cart=db.query(models.Cart).all()
    return cart






