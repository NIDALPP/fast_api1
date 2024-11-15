from fastapi import APIRouter,Depends,status
from ..import schemas,database,oauth2,models
from sqlalchemy.orm import Session
from ..repository import product
from typing import  List



router=APIRouter(
    prefix='/product',
    tags=['MANAGE PRODUCTS']
)

get_db=database.get_db


@router.post('/',response_model=schemas.ProductCreate)
def create_product(request: schemas.ProductCreate,db: Session=Depends(get_db), current_user: models.User = Depends(oauth2.get_admin_user)):
    return product.create_product(db,request)

@router.get('/',response_model=List[schemas.Product])
def all(db: Session=Depends(get_db), current_user: models.User = Depends(oauth2.get_admin_user)):
    return product.get_all(db)


@router.delete('/{id}')
def destroy(id:int,db: Session=Depends(get_db), current_user: models.User = Depends(oauth2.get_admin_user)):
    return product.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.ProductBase,db: Session=Depends(get_db), current_user: models.User = Depends(oauth2.get_admin_user)):
    return product.update(id,request,db)