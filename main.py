from fastapi import FastAPI
from routes.products import routerProducts

app = FastAPI(title='API products', description='api rest python and fastapi', version='0.0.1')

# Incluimos las rutas
app.include_router(routerProducts)