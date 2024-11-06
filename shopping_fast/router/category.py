from fastapi import APIRouter,Depends,status
from ..import schemas,database,oauth2
from sqlalchemy.orm import Session
from ..repository import category
from typing import  List


router=APIRouter(
    prefix='/category',
    tags=['Manage category']
)

get_db=database.get_db

@router.post("/", response_model=schemas.CategoryCreate)
def create_category(request: schemas.CategoryCreate, db: Session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_admin_user)):
    return category.create_category(db, request)

@router.get('/',response_model=List[schemas.CategoryBase])
def all(db: Session=Depends(get_db)):
    return category.get_all(db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db: Session=Depends(get_db)):
    return category.destroy(id,db)
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.CategoryBase,db: Session=Depends(get_db)):
    return category.destroy(id,request,db)