from sqlalchemy.orm import Session
from .. import models,schemas
# from fastapi import Depends
# from ..database import get_db



def create( db: Session,request: schemas.Admin):
    new_admin = models.Admin(name=request.name, email=request.email, password=request.password,role=request.role)
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


def show_all(db: Session):
    admin=db.query(models.Admin).all()
    return admin

def delete(id:int,db: Session):
    adm=db.query(models.Admin).filter(models.Admin.admin_id==id)
    adm.first()
    adm.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id:int,redb: Session):
    adm=db.query(models.Admin).filter(models.Admin.admin_id==id)
