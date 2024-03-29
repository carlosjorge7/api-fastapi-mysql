from sqlalchemy import create_engine, MetaData
from config.enviroment import DB_HOST, DB_USER, DB_NAME, DB_PORT, DB_PASSWORD

# LOCAL
DATABASE_URL = 'mysql+pymysql://'+DB_USER+':'+DB_PASSWORD+'@'+DB_HOST+':'+DB_PORT+'/'+DB_NAME

ssl_args = {
    "ssl": {
        "ca": "/home/carlos/Escritorio/api-fastapi-mysql/ca.pem"
    }
}

engine = create_engine(DATABASE_URL, pool_pre_ping=True, connect_args=ssl_args)
meta = MetaData(bind=engine)

conn = engine.connect()