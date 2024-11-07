from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm


from .. import database, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session
router = APIRouter(tags=['Authentication'])



@router.post('/admin/login')
def login_admin(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    admin = db.query(models.User).filter(models.User.email == request.username,models.User.role=="ADMIN").first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Invalid Credentials')
    if not Hash.verify(admin.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='incorrect Password')
            
    access_token=token.create_access_token(data={'sub':admin.email,"role":"ADMIN"})
    return {"access_token":access_token,"token_type":"bearer"}

@router.post('/customer/login')
def login_customer(request: OAuth2PasswordRequestForm=Depends(),db: Session=Depends(database.get_db)):
    customer=db.query(models.User).filter(models.User.email== request.username,models.User.role=="CUSTOMER").first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Invalid credentials')
    if not Hash.verify(customer.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='incorrect Password')
    access_token=token.create_access_token(data={'sub':customer.email,"role":"CUSTOMER"})
    return {"access_token":access_token,"token_type":"bearer"}