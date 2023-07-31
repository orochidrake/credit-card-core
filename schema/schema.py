from pydantic import BaseModel
from typing import Optional
from enum import Enum
from dataclasses import dataclass


class Role(str,Enum):
    USER = "user"
    MANAGER = "manager"
    ADMIN = "admin"

@dataclass
class SignUser:
    fullname: str
    email: str
    role: Role


class NewUser(BaseModel):
    fullname: str
    email: str
    password: str
    role:Role

    class ConfigDict:
        from_attributes = True

class ResUser(BaseModel):
    id: int
    fullname: str
    email: str
    role: Role
    date: str
    time: str
 

    class ConfigDict:
        from_attributes = True

class Login(BaseModel):
    email: str
    password: str

    class ConfigDict:
        from_attributes = True