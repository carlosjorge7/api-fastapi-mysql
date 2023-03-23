from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta

products = Table('products', meta, 
                Column('id', Integer, primary_key=True), 
                Column('name', String(50)),
                Column('description', String(50))
                )

users = Table('users', meta, 
                Column('id', Integer, primary_key=True), 
                Column('username', String(50)),
                Column('email', String(50)),
                Column('password', String(100))
                )

meta.create_all(engine)