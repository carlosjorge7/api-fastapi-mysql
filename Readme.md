# api in fastapi

# create enviroment and activate

virtualenv env
source ./env/Scripts/activate

# download dependencies

pip install -r requirements.txt

# run server

uvicorn main:app --host="127.0.0.1" --port="3000" --reload

# next step

Variables de entorno, conectar con algun servicio de mysql gratis, desplegar la api
