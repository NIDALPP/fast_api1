from fastapi import FastAPI
from .database import engine,Base
from . import models
from . router import admin,category,product,customer,authentication

app=FastAPI()
# models.Base.metadata.drop_all(engine)

models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(admin.router)
app.include_router(customer.router)
app.include_router(category.router)
app.include_router(product.router)



