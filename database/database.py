from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLITE_DATA_BASE_URL = "sqlite:///./database.db"

engine = create_engine(
  SQLITE_DATA_BASE_URL, echo=True, connect_args={"check_same_thread": False}
)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
  db = Sessionlocal()
    try:
      yield db
    finally:
      db.close()