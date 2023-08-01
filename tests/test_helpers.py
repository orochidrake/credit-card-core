from argon2 import PasswordHasher
from utils.helpers import encode_credit_card_number, decode_credit_card_number, full_exp_date, hash_password, verify_hashed_password
import pytest

ph = PasswordHasher()

@pytest.mark.asyncio
async def test_hash_password():
    password = "password123"
    hashed_password = await hash_password(password)
    assert hashed_password is not None
    assert len(hashed_password) > 0

@pytest.mark.asyncio
async def test_verify_hashed_password():
    password = "password123"
    hashed_password = ph.hash(password)
    is_valid = await verify_hashed_password(password, hashed_password)
    assert is_valid is True

    incorrect_password = "incorrect"
    is_valid = await verify_hashed_password(incorrect_password, hashed_password)
    assert is_valid is False



@pytest.mark.asyncio
async def test_full_exp_date():
    assert await full_exp_date('12/2022') == date(2022, 12, 31)

@pytest.mark.asyncio
async def test_encode_credit_card_number():
    assert await encode_credit_card_number("4793787187097048") == "Qka3k8kk8k0ak0Q8"
    

@pytest.mark.asyncio
async def test_decode_credit_card_number():
    assert await decode_credit_card_number("Qka3k8kk8k0ak0Q8") == "4793787187097048"