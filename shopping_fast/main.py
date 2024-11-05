from fastapi import FastAPI
from .database import engine
from . import models
from . router import admin,manage

app=FastAPI()
# models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)

app.include_router(admin.router)
app.include_router(manage.router)

