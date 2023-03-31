from fastapi import APIRouter, HTTPException
from jose import JWTError, jwt
from config.db import conn
from models.models import users
from schemas.schemas import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
usersRouter = APIRouter(prefix='/users')

@usersRouter.post('/register', response_model = User)
def create_user(user: User):
    new_user = {'username': user.username, 'email': user.email, 'password': hash_password(user.password)}
    res = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == res.lastrowid)).first()

@usersRouter.post('/login')
async def login(user: User):
    user = authenticate_user(user.username, user.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = jwt.encode({'userId': user.id}, 'secret', algorithm="HS256")
    return {"access_token": user.username, "token": token}

#Fuctions
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not pwd_context.verify(password, user.password):
        return False
    return user

def get_user(username: str):
    user = conn.execute(users.select().where(users.c.username == username)).first()
    if user:
        return User(**user)
    else:
        return None
    
def hash_password(password: str):
    return pwd_context.hash(password)

def authenticate_token(token: str):
    try:
        payload = jwt.decode(token, 'secret', algorithms="HS256")
        userId = payload.get('userId')
        if userId is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    return userId