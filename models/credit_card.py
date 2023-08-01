
from sqlalchemy import String,Integer,Column,Text,Date, DateTime
from database.database import Base

class User(Base):
    __tablename__='credit_cards'
    id=Column(Integer,primary_key=True)
    exp_date=Column(Date,nullable=False)
    holder=Column(Text,nullable=False,unique=True)
    number=Column(String(255),nullable=False)
    cvv=Column(Integer,nullable=True)
    brand=Column(String(255),nullable=False)
    created_at=Column(DateTime(timezone=True))
    