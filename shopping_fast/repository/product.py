from sqlalchemy.orm import Session
from .. import models,schemas

def create_product(db:Session,request: schemas.ProductCreate):
    new_product = models.Products(name=request.name,price=request.price,description=request.description,cat_id=request.cat_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product