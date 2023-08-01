from pydantic import BaseModel
from datetime import datetime, date
from dataclasses import dataclass


@dataclass
class NewCreditCard(BaseModel):
    exp_date: str
    holder: str
    number: str
    cvv: int

    class ConfigDict:
        from_attributes = True

class ResponseCreditCard(BaseModel):
    id: int
    exp_date: date
    holder: str
    number: str
    cvv: int
    brand: str
    created_at: datetime

    class ConfigDict:
        from_attributes = True

class ResponseUpdateCreditCard(BaseModel):
    id: int
    exp_date: date
    holder: str
    number: str
    cvv: int
    brand: str
    created_at: datetime
    

    class ConfigDict:
        orm_mode = True

class DeletionCreditCardSuccess(BaseModel):
    status: str = "Success"
    message: str = "Credit Card deleted successfully."