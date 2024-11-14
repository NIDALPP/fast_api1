# from sqlalchemy.orm import Session
# from .. import schemas, database, models, oauth2
# from .. repository import manage_order
# router = APIRouter(
#     tags=["manage_order"]
# )
# get_db = database.get_db

# @router.post("/", response_model=schemas.Order)
# def place_order(db: Session = Depends(get_db), user: models.User = Depends(oauth2.get_customer_user)):
#     order_repo_instance = manage_order.OrderCreate(db)
    
#     cart = db.query(models.CartItem).filter(models.CartItem.user_id == user.user_id).all()
#     if not cart:
#         raise HTTPException(status_code=404, detail="Cart not found")

#     try:
#         order = order_repo_instance.create_order(user.user_id, cart.cart_id)
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
    
#     return order



from fastapi import APIRouter, Depends, HTTPException,status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2
from .. repository import manage_order
router = APIRouter(
    tags=["manage_order"]
)
get_db = database.get_db

@router.post("/", response_model=schemas.Order)
def place_order(db: Session = Depends(get_db), user: models.User = Depends(oauth2.get_customer_user)):
    order_repo_instance = manage_order.OrderCreate(db)
    
    cart = db.query(models.Cart).filter(models.Cart.user_id == user.user_id).first()
    
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    try:
        order = order_repo_instance.create_order(user.user_id, cart.cart_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return order

@router.get('/',response_model=List[schemas.Order])
def all(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_admin_user)):
    orders = manage_order.get_all(db)  
    
    return orders