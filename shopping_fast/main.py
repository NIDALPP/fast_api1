from fastapi import FastAPI
from .database import engine,Base
from . import models
from . router import category,product,authentication,cart, user,order

app=FastAPI()
# models.Base.metadata.drop_all(engine)

models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(category.router)
app.include_router(product.router)
app.include_router(order.router)
app.include_router(cart.router)



