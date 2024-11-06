from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from . import token





oauth2_admin_scheme = OAuth2PasswordBearer(tokenUrl="admin/login")


def get_admin_user(data: str=Depends(oauth2_admin_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user= token.verify_token(data,credentials_exception)
    if user["role"]!="ADMIN":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not an admin")
    return user



oauth2_customer_scheme = OAuth2PasswordBearer(tokenUrl="customer/login")

def get_customer_user(data: str = Depends(oauth2_customer_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = token.verify_token(data, credentials_exception)
    if user["role"] != "CUSTOMER":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return user