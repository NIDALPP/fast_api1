from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2
from sqlalchemy.orm import Session
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel, OAuthFlowPassword as OAuthFlowPasswordModel
from . import token, database, models

class OAuth2PasswordBearerAdmin(OAuth2):
    def __init__(self, tokenUrl: str):
        flows = OAuthFlowsModel(password=OAuthFlowPasswordModel(tokenUrl=tokenUrl))
        super().__init__(flows=flows)
oauth2_scheme_admin = OAuth2PasswordBearerAdmin(tokenUrl="admin/login")


def get_admin_user(db: Session = Depends(database.get_db), data: str = Depends(oauth2_scheme_admin)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )   
    
    token_str = data.replace("Bearer ", "") if data.startswith("Bearer ") else data

    payload = token.verify_token(token_str, credentials_exception)
    user = db.query(models.User).filter(models.User.email == payload.get("username")).first()
    if user is None or user.role != "ADMIN":
        raise credentials_exception
    return user

class OAuth2PasswordBearerCustomer(OAuth2):
    def __init__(self, tokenUrl: str):
        flows = OAuthFlowsModel(password=OAuthFlowPasswordModel(tokenUrl=tokenUrl))
        super().__init__(flows=flows)

oauth2_scheme_customer = OAuth2PasswordBearerCustomer(tokenUrl="customer/login")

def get_customer_user(db: Session = Depends(database.get_db), data: str = Depends(oauth2_scheme_customer)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_str = data.replace("Bearer ", "") if data.startswith("Bearer ") else data
    
    payload = token.verify_token(token_str, credentials_exception)
    
    user = db.query(models.User).filter(models.User.email == payload.get("username")).first()
    if user is None or user.role != "CUSTOMER":
        raise credentials_exception
    return user
