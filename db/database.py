from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE

DB_USERNAME = "postgres"
DB_PASSWORD = "AcademyRootPassword"
DB_HOSTNAME = "localhost"
DB_PORT = "5432"
DATABASE = "main_backendproject"
DB_URL = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DATABASE}"
# CREATE ENGINE
engine = create_engine(DB_URL)
# CREATE SESSION
Sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
# CREATE BASE
Base = declarative_base()