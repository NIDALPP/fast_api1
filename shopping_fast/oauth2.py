from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer,OAuth2
from sqlalchemy.orm import Session
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel, OAuthFlowPassword as OAuthFlowPasswordModel
from . import token, database, models

# class OAuth2PasswordBearerAdmin(OAuth2):
#     def __init__(self, tokenUrl: str):
#         flows = OAuthFlowsModel(password=OAuthFlowPasswordModel(tokenUrl=tokenUrl))
#         super().__init__(flows=flows)
# oauth2_scheme_admin = OAuth2PasswordBearerAdmin(tokenUrl="admin/login")


# def get_admin_user(db: Session = Depends(database.get_db), token: str = Depends(oauth2_scheme_admin)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     payload = token.verify_token(token, credentials_exception)
#     user = db.query(models.User).filter(models.User.email == payload.get("sub")).first()
#     if user is None or user.role != "ADMIN":
#         raise credentials_exception
#     return user

# class OAuth2PasswordBearerCustomer(OAuth2):
#     def __init__(self, tokenUrl: str):
#         flows = OAuthFlowsModel(password=OAuthFlowPasswordModel(tokenUrl=tokenUrl))
#         super().__init__(flows=flows)

# oauth2_scheme_customer = OAuth2PasswordBearerCustomer(tokenUrl="customer/login")

# def get_customer_user(db: Session = Depends(database.get_db), token: str = Depends(oauth2_scheme_customer)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     payload = token.verify_token(token, credentials_exception)
#     user = db.query(models.User).filter(models.User.email == payload.get("sub")).first()
#     if user is None or user.role != "CUSTOMER":
#         raise credentials_exception
#     return user




from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
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
    payload = token.verify_token(data, credentials_exception)
    user = db.query(models.User).filter(models.User.email == payload.get("sub")).first()
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
    
    try:
    
        payload = token.verify_token(data, credentials_exception)
        print(f"Payload: {payload}") 
        user = db.query(models.User).filter(models.User.email == payload.get("sub")).first()
        
        if user is None or user.role != "CUSTOMER":
            print(f"User not found or invalid role")  
            raise credentials_exception
        
        return user
    except HTTPException as e:
        print(f"HTTPException in get_customer_user: {e}")
        raise e





