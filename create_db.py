from database.database import Base,engine
from models.user import User

print("Creating database ....")

Base.metadata.create_all(engine)