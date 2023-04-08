from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta

users = Table('users', meta, 
                Column('id', Integer, primary_key=True), 
                Column('username', String(50)),
                Column('email', String(50)),
                Column('password', String(100))
                )

products = Table('products', meta, 
                Column('id', Integer, primary_key=True), 
                Column('name', String(50)),
                Column('description', String(50)),
                Column('user_id', Integer, ForeignKey('users.id'))
                )

meta.create_all(engine)