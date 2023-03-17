from fastapi import APIRouter, Response
from config.db import conn
from models.products import products
from schemas.product import Product

routerProducts = APIRouter(prefix='/products')

@routerProducts.get('/', response_model = list[Product])
def get_products():
    return conn.execute(products.select()).fetchall()

@routerProducts.post('/', response_model = Product)
def create_user(product: Product):
    new_product = {'name': product.name, 'description': product.description}
    res = conn.execute(products.insert().values(new_product))
    return conn.execute(products.select().where(products.c.id == res.lastrowid)).first()

@routerProducts.get('/{id}', response_model = Product)
def get_product(id: str):
    res = conn.execute(products.select().where(products.c.id == id)).first()
    return res

@routerProducts.delete('/{id}', status_code = 200)
def delete_user(id: str):
    conn.execute(products.delete().where(products.c.id == id))
    return Response(status_code=200)

@routerProducts.put('/{id}', response_model = Product)
def update_user(id: str, product: Product):
    conn.execute(products.update()
                        .values(name = product.name, description = product.description)
                        .where(products.c.id == id))
    return conn.execute(products.select().where(products.c.id == id)).first()




