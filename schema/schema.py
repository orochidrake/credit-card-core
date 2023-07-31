from pydantic import BaseModel
from typing import Optional
from enum import Enum
from dataclasses import dataclass


class Role(str,Enum):
    USER = "user"
    MANAGER = "manager"
    ADMIN = "admin"