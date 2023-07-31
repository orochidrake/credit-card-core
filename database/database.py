from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import settings
from sqlalchemy.util import deprecations


deprecations.SILENCE_UBER_WARNING = True
POSTGRES_PASSWORD = settings.POSTGRES_PASSWORD
POSTGRES_USER = settings.POSTGRES_USER
POSTGRES_DB=settings.POSTGRES_DB

url_object = URL.create(
    "postgresql",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host="localhost",
    database=POSTGRES_DB,
)

engine = create_engine(
  url_object
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()