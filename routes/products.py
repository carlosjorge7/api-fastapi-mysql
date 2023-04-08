from fastapi import APIRouter, Response, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config.db import conn
from models.models import products
from routes.users import authenticate_token
from schemas.schemas import Product

routerProducts = APIRouter(prefix='/products')

bearer = HTTPBearer()

# def validateToken(token: HTTPAuthorizationCredentials = Depends(bearer)):
#     return authenticate_token(token.credentials)

@routerProducts.get('/', response_model = list[Product])
async def get_products(token: HTTPAuthorizationCredentials = Depends(bearer)):
    userId = authenticate_token(token.credentials)
    print(userId)
    return conn.execute(products.select()).fetchall()

@routerProducts.post('/', response_model = Product)
async def create_product(product: Product, token: HTTPAuthorizationCredentials = Depends(bearer)):
    user_id = authenticate_token(token.credentials)
    new_product = {'name': product.name, 'description': product.description, 'user_id': user_id}
    res = conn.execute(products.insert().values(new_product))
    return conn.execute(products.select().where(products.c.id == res.lastrowid)).first()

@routerProducts.get('/{id}', response_model = Product)
def get_product(id: str):
    res = conn.execute(products.select().where(products.c.id == id)).first()
    return res

@routerProducts.delete('/{id}', status_code = 200)
def delete_product(id: str):
    conn.execute(products.delete().where(products.c.id == id))
    return Response(status_code=200)

@routerProducts.put('/{id}', response_model = Product)
def update_product(id: str, product: Product):
    conn.execute(products.update()
                        .values(name = product.name, description = product.description)
                        .where(products.c.id == id))
    return conn.execute(products.select().where(products.c.id == id)).first()





