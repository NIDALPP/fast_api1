from fastapi import APIRouter,Depends,status
from ..import schemas,database,oauth2
from sqlalchemy.orm import Session
from ..repository import cart
from typing import  List


router=APIRouter(
    prefix='/cart',
    tags=['manage cart']
)


get_db=database.get_db




@router.get('/',response_model=List[schemas.Cart])
def all(db: Session=Depends(get_db)):
    return cart.get_all(db)





