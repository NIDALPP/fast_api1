from fastapi import APIRouter,Depends,status
from ..import schemas,database,oauth2,models
from sqlalchemy.orm import Session
from ..repository import cart
from typing import  List


router=APIRouter(
    prefix='/cart',
    tags=['LIST OF CARTS']
)


get_db=database.get_db




@router.get('/',response_model=List[schemas.Cart])
def all(db: Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_admin_user)):
    return cart.get_all(db)





