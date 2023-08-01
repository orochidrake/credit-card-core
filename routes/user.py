from fastapi import status, HTTPException, APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from database.database import SessionLocal
from models.user import User
from schema.schema import NewUser,ResponseUser, Role, Login
from datetime import datetime
from typing import List
from auth.auth import sign_jwt
from auth.auth import decode_jwt
from sqlalchemy.exc import SQLAlchemyError
from utils.helpers import hash_password,verify_hashed_password

# Create a database session
db = SessionLocal()

# Create an API router
router = APIRouter()

# Define the OAuth2 password bearer scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


# Endpoint for creating a new user
@router.post('/api/v1/signup/', response_model=ResponseUser, status_code=status.HTTP_201_CREATED)
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
            created_at=datetime.now(),
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

# Endpoint for user login
@router.post('/api/v1/login/')
async def login_a_user(login: Login):
    try:
        db_user = db.query(User).filter(User.email == login.email).first()

        if db_user is not None:
            # Verify the user's password
            is_password_valid = await verify_hashed_password(login.password, db_user.password)

            if not is_password_valid:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You have entered a wrong password")
            
            if is_password_valid:
                # Generate a JWT access token for authentication
                token = sign_jwt(db_user)
                return token
            else:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You have entered a wrong password")
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found in the database")

# Utility function to get user from token
async def get_user_from_token(token: str):
    user_from_token = decode_jwt(token)
    if not user_from_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    return user_from_token



# Endpoint for retrieving a list of users
@router.get('/api/v1/users/', response_model=List[ResponseUser], status_code=200)
async def get_users(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    token: str = Depends(oauth2_scheme)
):
    try:
        user_from_token = await get_user_from_token(token)
        role = Role(user_from_token['role'])
        user_email = user_from_token['user_email']
        offset = (page - 1) * per_page

        if role == Role.ADMIN:
            user_entries = db.query(User).offset(offset).limit(per_page).all()
        elif role == Role.MANAGER:
            user_entries = db.query(User).filter(User.role == Role.USER).offset(offset).limit(per_page).all()
        elif role == Role.USER:
            user_entries = db.query(User).filter(User.email == user_email).first()
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient privileges")
        print(user_entries)
        return user_entries
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Export the router
user_routes = router