from fastapi import APIRouter,Depends,status
from ..import schemas,database,oauth2,models
from sqlalchemy.orm import Session
from ..repository import category
from typing import  List


router=APIRouter(
    prefix='/category',
    tags=['Manage category']
)

get_db=database.get_db

@router.post("/", response_model=schemas.Category)
def create_category(request: schemas.CategoryCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_admin_user)):
    return category.create_category(db, request)
@router.get('/',response_model=List[schemas.Category],)
def all(db: Session=Depends(get_db), current_user: models.User = Depends(oauth2.get_admin_user)):
    return category.get_all(db)

@router.delete('/{id}')
def destroy(id:int,db: Session=Depends(get_db), current_user: models.User = Depends(oauth2.get_admin_user)):
    return category.destroy(id,db)
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.CategoryBase,db: Session=Depends(get_db), current_user: models.User = Depends(oauth2.get_admin_user)):
    return category.update(id,request,db)