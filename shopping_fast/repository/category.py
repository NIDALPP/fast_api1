from sqlalchemy.orm import Session
from .. import models,schemas


def create_category(db: Session, request: schemas.CategoryCreate):
    db_category = models.Category(name=request.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_all(db: Session):
    cat=db.query(models.Category).all()
    return cat