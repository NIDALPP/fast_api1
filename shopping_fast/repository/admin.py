from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status
from ..hashing import Hash


def create(request: schemas.User,db: Session):
    if request.role not in ["ADMIN", "CUSTOMER"]:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="only ADMIN or CUSTOMER is accepted")
    new_admin = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password),role=request.role,phone=request.phone,address=request.address)
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


def show_all(db: Session):
    admin=db.query(models.User).all()
    return admin

def destroy(id:int,db: Session):
    adm=db.query(models.User).filter(models.User.user_id==id)
    if not adm.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"admin with the id {id} not found")
    adm.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(db: Session,id:int,request: schemas.User):
    adm=db.query(models.User).filter(models.User.user_id==id)
    if not adm.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'admin with the id {id} not found')
    for key,value in request.dict().items():
        setattr(adm, key, value)
    adm.update(request)
    db.commit()
    return 'updated'
