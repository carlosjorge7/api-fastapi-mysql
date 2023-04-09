from sqlalchemy import create_engine, MetaData
from config.enviroment import DB_HOST, DB_USER, DB_NAME, DB_PASSWORD, MYSQL_ATTR_SSL_CA

# DESARROLLO
DATABASE_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4&ssl_ca={MYSQL_ATTR_SSL_CA}'

# LOCAL
# DATABASE_URL = 'mysql+pymysql://'+DB_USER+'@'+DB_HOST+':'+DB_PORT+'/'+DB_NAME

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
meta = MetaData(bind=engine)

conn = engine.connect()