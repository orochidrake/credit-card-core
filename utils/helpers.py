
from fastapi import HTTPException
import calendar
from datetime import date
#chose argon2 for improved resitance against attacks
from argon2 import PasswordHasher
import argon2.exceptions
from creditcard import CreditCard

ph = PasswordHasher()
alphabets = 'loaCe75e6n&kG%kEOQ%^aOuQaG&qBPEjkQ1nI4n#zUVqrIM@@^U!uhi#Eh!QEY*%GBJd^WPRkU9k#MOLVe9l$kPC2@bulq^V^lA'
async def hash_password(password: str):
    hashed_password = ph.hash(password)
    return hashed_password

async def verify_hashed_password(password:str,hashed_password: str):
    try:
        is_password_valid = ph.verify(hashed_password, password)
        return is_password_valid
    except argon2.exceptions.VerifyMismatchError:
        return False
    
async def full_exp_date(item: str):
  date_temp = item.split('-')
  res = calendar.monthrange(int(date_temp[0]), int(date_temp[1]))
  day = res[1]
  return date(int(date_temp[0]), int(date_temp[1]), int(day))

  
async def encode_credit_card_number(number: str):
    results = ''
    for k in number:
      try:
        i = (alphabets.index(k) + 6) % 26
        results += alphabets[i]
      except ValueError:
        results+= k
    return results

async def decode_credit_card_number(number: str):
  results = ''
  for k in number:
    try:
      i = (alphabets.index(k) - 6) % 26
      results +=alphabets[i]
    except ValueError:
      results += k
  return results.lower()

async def check_number_is_valid(card_number:str):
    cc = CreditCard(card_number)
    if cc.is_valid():
      return cc.is_valid() 
    else:
      raise HTTPException(status_code=400, detail="Credit card number invalid")
    
async def get_credit_brand(card_number:str):
    cc = CreditCard(card_number)
    try:
      return cc.get_brand() 
    except:
        raise HTTPException(status_code=404, detail="Card number does not match any brand")
    
    
    

    