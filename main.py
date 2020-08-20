from fastapi import FastAPI, Request, Depends, BackgroundTasks
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import User
import sqlalchemy
import uvicorn
import datetime
import models
import bcrypt

DATABASE_URI = "sqlite:///./database.db"
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class User_model(BaseModel):
    username:str
    password:str
    date_registed:datetime.datetime=datetime.datetime.utcnow()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def index():
    return {"message":"hello world"}

@app.get("/login/")
async def login(user:User_model):
    db = SessionLocal()
    user_vals = db.query(User).filter(User.username==user.username).first()
    if bcrypt.checkpw(user.password.encode(), user_vals.hashed_pword):
        return {"ok":"signed in"}
    else:
        return {"error":"incorrect password"}

@app.get("/register/")
async def create_user(user:User_model, db: Session = Depends(get_db)):
    user_sent = User()
    user_sent.username = user.username
    user_sent.hashed_pword = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    db.add(user_sent)
    db.commit()
    return {"ok":"user created"}

if __name__ == "__main__":
    uvicorn.run(app,host='0.0.0.0',port=5000, log_level="info")