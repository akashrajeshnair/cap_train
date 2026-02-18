from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import time

# Connect to MySQL server using root (more reliable for initial setup)
BASE_CONNECTION_STRING = 'mysql+pymysql://root:rootpassword@mysql:3306'

# Wait for MySQL to be ready
max_retries = 30
retry_count = 0
engine = None

while retry_count < max_retries:
    try:
        engine = create_engine(BASE_CONNECTION_STRING, echo=True)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Successfully connected to MySQL")
        break
    except Exception as e:
        retry_count += 1
        print(f"Waiting for MySQL... ({retry_count}/{max_retries}): {e}")
        time.sleep(2)
        if retry_count >= max_retries:
            raise Exception("Could not connect to MySQL after 30 attempts")

# Create database if it doesn't exist
db_name = 'banking'
db_status = False

try:
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        connection.commit()
        print(f"Database {db_name} created successfully")
        db_status = True
except Exception as e:
    print("Could not initialize database: ", e)

# Now connect to the specific database
if db_status:
    DATABASE_URL = BASE_CONNECTION_STRING + f'/{db_name}'
    engine = create_engine(DATABASE_URL, echo=True)
    session_local = sessionmaker(bind=engine)
    print('Database connection established.')
else:
    raise Exception('Can\'t create database due to internal error.')