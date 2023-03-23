from fastapi import FastAPI

from routes.products import routerProducts
from routes.users import usersRouter

# Insyalcia del servidor
app = FastAPI(title='API RESTful with FastAPI and MYSQL',
            description='api rest python', 
            version='0.0.2')

# Incluimos las rutas
app.include_router(routerProducts)
app.include_router(usersRouter)