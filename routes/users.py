from fastapi import APIRouter, HTTPException, Depends
from config.db import conn
from models.models import users
from schemas.schemas import User
from passlib.context import CryptContext
from fastapi_jwt_auth import AuthJWT

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

usersRouter = APIRouter(prefix='/users')

@usersRouter.post('/create_user', response_model = User)
async def create_user(user: User):
    new_user = {'username': user.username, 'email': user.email, 'password': hash_password(user.password)}
    res = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == res.lastrowid)).first()


def hash_password(password: str):
    return pwd_context.hash(password)