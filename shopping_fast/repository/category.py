from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status


def create_category(db: Session, request: schemas.CategoryCreate):
    db_category = models.Category(name=request.name,active=request.active,parent_category_id=request.parent_category_id,icon=request.icon)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_all(db: Session):
    cat=db.query(models.Category).all()
    return cat

def destroy(id:int,db: Session):
    cat=db.query(models.Category).filter(models.Category.cat_id==id)
    if not cat.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Category with id {id} not found")
    cat.delete(synchronize_session=False)
    db.commit()
    return "done"    






def update(id:int,request: schemas.CategoryBase,db: Session):
    cat=db.query(models.Category).filter(models.Category.cat_id==id).first()
    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'admin with the id {id} not found')
    for key,value in request.dict().items():
        setattr(cat, key, value)
    db.commit()
    return {"details":"updated successfully"}