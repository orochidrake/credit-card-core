from fastapi import status, HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from database.database import SessionLocal
from models.credit_card import CreditCard
from routes.user import get_user_from_token
from schema.credit_card_schema import NewCreditCard,ResponseCreditCard
from datetime import date, datetime
from typing import List
from schema.user_schema import Role
from sqlalchemy.exc import SQLAlchemyError
from utils.helpers import check_number_is_valid, encode_credit_card_number, full_exp_date, get_credit_brand

db = SessionLocal()
router = APIRouter()

# Define the OAuth2 password bearer scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

# Create Credit Card Method
@router.post('/api/v1/credit-card/', response_model=ResponseCreditCard, status_code=status.HTTP_201_CREATED)
async def create_credit_card(credit_card: NewCreditCard, token: str = Depends(oauth2_scheme)):
    try:
        user_from_token = await get_user_from_token(token)
        role = Role(user_from_token['role'])

        if not role:
            raise HTTPException(status_code=status.HTTP_401_FORBIDDEN, detail="Invalid or expired token")
        
        await check_number_is_valid(credit_card.number)
            

        hashed_number = await encode_credit_card_number(credit_card.number)
        brand =  await get_credit_brand(credit_card.number)

        present = datetime.now().date()
        exp_date = await full_exp_date(credit_card.exp_date)

        if exp_date < present:
            raise HTTPException(status_code=400, detail="The Expiration date is invalid")

        if credit_card.holder is None or len(credit_card.holder) <= 2:
            raise HTTPException(status_code=400, detail="The Credit Card Holder is invalid")
        
        if credit_card.cvv is None or len(str(credit_card.cvv)) < 3 or len(str(credit_card.cvv)) > 4 :
            raise HTTPException(status_code=400, detail="The Credit Card CVV is invalid")

        new_credit_card = CreditCard(
            exp_date=exp_date,
            holder=credit_card.holder,
            number=hashed_number,
            cvv=credit_card.cvv,
            brand=brand,
            created_at=datetime.now(),
        )
      
        db_item = db.query(CreditCard).filter(CreditCard.number == new_credit_card.number).first()
        
        if db_item is not None:
            raise HTTPException(status_code=409, detail="Credit card with the number already exists")

        db.add(new_credit_card)
        db.commit()

        return new_credit_card
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="An error occurred while creating the credit card")
    

credit_card_routes = router