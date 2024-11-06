from fastapi import APIRouter,Depends
from ..import schemas,database
from sqlalchemy.orm import Session
from ..repository import product
from typing import  List


router=APIRouter(
    prefix='/product',
    tags=['PRODUCTS']
)

get_db=database.get_db


@router.post('/',response_model=schemas.Product)
def create_product(request: schemas.ProductCreate,db: Session=Depends(get_db)):
    return product.create_product(db,request)