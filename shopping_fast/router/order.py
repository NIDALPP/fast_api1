from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..import schemas, database, models,oauth2
from .. repository import order
router = APIRouter()
get_db=database.get_db

@router.post("/add_to_cart/{product_id}")
def add_to_cart(
    product_id: int, 
    quantity: int, 
    db: Session = Depends(get_db), 
    user: models.User = Depends(oauth2.get_customer_user)):
    cart_repo = order.cart_create(db)

    product = cart_repo.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    cart = cart_repo.get_cart_by_user_id(user.user_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found for the user")

    cart_item = cart_repo.get_cart_item(cart.cart_id, product_id)

    if cart_item:
        updated_item = cart_repo.update_cart_item(cart_item, quantity)
        return {"message": "Product quantity updated", "cart_item": updated_item}
    else:
        new_cart_item = cart_repo.add_product_to_cart(cart.cart_id, product_id, quantity)
        return {"message": "Product added to cart", "cart_item": new_cart_item}
