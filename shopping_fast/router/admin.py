from fastapi import APIRouter,Depends,status,HTTPException
from ..import schemas,database
from sqlalchemy.orm import Session
from ..repository import admin
from typing import List



router=APIRouter(
    prefix='/user',
    tags=['USER']
)

get_db=database.get_db


@router.post('/signup',response_model=schemas.ShowUser,status_code=status.HTTP_201_CREATED)
def create_admin(request:schemas.User,db:Session=Depends(get_db)):
    return admin.create(request,db)

@router.get('/list',response_model=List[schemas.ShowUser])
def all(db: Session=Depends(get_db)):
    return admin.show_all(db)

@router.delete('/{id}')
def destroy(id:int,db: Session=Depends(get_db)):
    return admin.destroy(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request: schemas.User,db: Session=Depends(get_db)):
    return admin.update(db,id,request)