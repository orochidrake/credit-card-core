
from sqlalchemy import String,Integer,Column,Text, Enum, DateTime
from database.database import Base
from schema.user_schema import Role

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    fullname=Column(String(255),nullable=False)
    email=Column(Text,nullable=False,unique=True)
    password=Column(String(255),nullable=False)
    created_at=Column(DateTime(timezone=True))
    role=Column(Enum(Role))