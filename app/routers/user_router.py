from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.schemas import UserCreate
from passlib.context import CryptContext

router=APIRouter()

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_user(user:UserCreate,db:Session=Depends(get_db)):
    existing_user=db.query(User).filter(User.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already registered")
    
    hashed_password=pwd_context.hash(user.password)

    new_user=User(username=user.username,email=user.email,hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return{"message":"User registered successfully","user_id":new_user.id}