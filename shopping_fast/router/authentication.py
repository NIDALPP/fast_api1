from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session
router = APIRouter(tags=['Authentication'])



@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    admin = db.query(models.User).filter(models.User.email == request.username).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            details='Invalid Credentials')
    if not Hash.verify(admin.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                details='incorrect Password')
            
    access_token=token.create_access_token(data={'sub':admin.email})
    return {"access_token":access_token,"token_type":"bearer"}