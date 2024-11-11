from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status

def create_product(db:Session,request: schemas.ProductCreate):
    new_product = models.Product(name=request.name,price=request.price,description=request.description,
                                image_url=request.image_url,cat_id=request.cat_id,brand=request.brand,currency=request.currency,quantity=request.quantity,thumbnail=request.thumbnail)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_all(db: Session):
    pro=db.query(models.Product).all()
    return pro

def destroy(id:int,db: Session):
    pro=db.query(models.Product).filter(models.Product.product_id==id)
    if not pro.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"product with id {id} not found")
    pro.delete(synchronize_session=False)
    db.commit()
    return {'message':'product deleted'}




def update(id:int,request: schemas.ProductBase,db: Session):
    pro=db.query(models.Products).filter(models.Product.product_id==id).first()
    if not pro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'admin with the id {id} not found')
    for key,value in request.dict().items():
        setattr(pro, key, value)
    db.commit()
    return {"details":"updated successfully"}