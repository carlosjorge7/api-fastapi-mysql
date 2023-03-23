from fastapi import APIRouter, HTTPException
from config.db import conn
from models.models import users
from schemas.schemas import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

usersRouter = APIRouter(prefix='/users')

@usersRouter.post('/create_user', response_model = User)
async def create_user(user: User):
    new_user = {'username': user.username, 'email': user.email, 'password': hash_password(user.password)}
    res = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == res.lastrowid)).first()

@usersRouter.post("/login")
async def login(user: User):
    user = await authenticate_user(user.username, user.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"username": user.username, "password": user.password}


async def get_user(username: str):
    user = conn.execute(users.select().where(users.c.username == username)).first()
    if user:
        return User(**user)
    else:
        return None
    
async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user

def hash_password(password: str):
    return pwd_context.hash(password)