from fastapi import status, HTTPException, APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from database.database import SessionLocal
from models.user import User
from schema.schema import NewUser,ResUser, Role
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from utils.helpers import hash_password

# Create a database session
db = SessionLocal()

# Create an API router
router = APIRouter()

# Define the OAuth2 password bearer scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


# Endpoint for creating a new user
@router.post('/api/v1/signup/', response_model=ResUser, status_code=status.HTTP_201_CREATED)
async def create_a_user(user: NewUser):
    try:
        # Hash the user's password
        hashed_password = await hash_password(user.password)

        # Create a new user object
        new_user = User(
            fullname=user.fullname,
            email=user.email,
            password=hashed_password,
            role=user.role,
            date=datetime.now().strftime("%Y-%m-%d"),
            time=datetime.now().strftime("%H:%M:%S"),
        )

        # Check if a user with the same email already exists
        db_item = db.query(User).filter(User.email == new_user.email).first()

        if db_item is not None:
            raise HTTPException(status_code=409, detail="User with the email already exists")

        # Add the new user to the database
        db.add(new_user)
        db.commit()

        return new_user
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="An error occurred while creating the user")



# Export the router
user_routes = router