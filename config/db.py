from sqlalchemy import create_engine, MetaData
from .enviroment import DB_HOST, DB_USER, DB_PORT, DB_NAME

url = 'mysql+pymysql://'+DB_USER+'@'+DB_HOST+':'+DB_PORT+'/'+DB_NAME
engine = create_engine(url)

meta = MetaData()

conn = engine.connect()