from fastapi import APIRouter,Depends
from ..import schemas,database
from sqlalchemy.orm import Session
from ..repository import admin
from typing import List



router=APIRouter(
    prefix='/admin',
    tags=['users']
)

get_db=database.get_db


@router.post('/signup',response_model=schemas.Admin)
def create_admin(request:schemas.Admin,db:Session=Depends(get_db)):
    return admin.create(db,request)

@router.get('/list',response_model=List[schemas.ShowAdmin])
def all(db: Session=Depends(get_db)):
    return admin.show_all(db)

@router.delete('/{id}')
def destroy(id:int,db: Session=Depends(get_db)):
    return admin.delete(id,db)


@router.put('/{id}')
def update(id:int,db: Session=Depends(get_db)):
    return admin.update(id,db)


