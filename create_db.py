from database.database import Base,engine
from models.user import User
from models.credit_card import CreditCard

print("Creating database ....")

Base.metadata.create_all(engine)