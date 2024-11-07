from fastapi import APIRouter,Depends,status
from ..import schemas,database,oauth3
from sqlalchemy.orm import Session
from ..repository import cart
from typing import  List


router=APIRouter(
    prefix='/cart',
    tags=['manage cart']
)


get_db=database.get_db


@router.post('/create',response_model=schemas.cart,status_code=status.HTTP_201_CREATED)
def create_cart(request:schemas.cartCreate,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth3.get_customer_user)):
    return cart.create(request,db)