from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models, oauth2
from ..repository import order

router = APIRouter(
    prefix='/add to cart',
    tags=['cart ']
)
get_db = database.get_db

@router.post("/")
def add_to_cart(
    product_id: int, 
    quantity: int, 
    db: Session = Depends(get_db), 
    user: models.User = Depends(oauth2.get_customer_user)
):
    cart_repo = order.CartCreate(db)

    product = cart_repo.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    cart = cart_repo.get_cart_by_user_id(user.user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found for the user")

    cart_item = cart_repo.get_cart_item(cart.cart_id, product_id, user.user_id) 

    if cart_item:
        updated_item = cart_repo.update_cart_item(cart_item, quantity)
        return {"message": "Product quantity updated", "cart_item": updated_item}
    else:
        new_cart_item = cart_repo.add_product_to_cart(cart.cart_id, product_id, quantity, user.user_id)
        return {"message": "Product added to cart", "cart_item": new_cart_item}


@router.get("/cart_items", response_model=List[schemas.CartItem])
def get_cart_items(db: Session = Depends(get_db), user: models.User = Depends(oauth2.get_customer_user)):
    cart_repo = order.CartCreate(db)
    
    cart = cart_repo.get_cart_by_user_id(user.user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found for the user")
    
    cart_items = cart_repo.get_all_cart_items(cart.cart_id, user.user_id)
    return cart_items


@router.put("/update_cart_item")
def update_cart_item(
    cart_item_id: int, 
    quantity: int, 
    db: Session = Depends(get_db), 
    user: models.User = Depends(oauth2.get_customer_user)
):
    cart_repo = order.CartCreate(db)
    
    cart_item = cart_repo.get_cart_item(cart_item_id=cart_item_id, user_id=user.user_id, cart_id=None)

    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    updated_item = cart_repo.update(cart_item, quantity)
    
    return {"message": "Product quantity updated", "cart_item": updated_item}

@router.delete("/clear_cart")
def clear_cart(db: Session = Depends(get_db), user: models.User = Depends(oauth2.get_customer_user)):
    cart_repo = order.CartCreate(db)
    
    cart = cart_repo.get_cart_by_user_id(user.user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found for the user")
    
    cart_repo.clear_cart(cart.cart_id)
    return {"message": "Cart cleared successfully"}



