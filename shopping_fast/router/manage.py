from fastapi import APIRouter,Depends
from ..import schemas,database
from sqlalchemy.orm import Session
from ..repository import category,product
from typing import  List


router=APIRouter(
    tags=['manage products']
)

get_db=database.get_db

@router.post("/categories", response_model=schemas.Category)
def create_category(request: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return category.create_category(db, request)

@router.get('/',response_model=List[schemas.CategoryBase])
def all(db: Session=Depends(get_db)):
    return category.get_all(db)



@router.post('/products',response_model=schemas.Product)
def create_product(request: schemas.ProductCreate,db: Session=Depends(get_db)):
    return product.create_product(db,request)