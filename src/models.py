from datetime import datetime
from pydantic import BaseModel


# Auth
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str


class UserInDB(User):
    hashed_password: str


# Web pages
class Parafia(BaseModel):
    id: int
    nazwa: str

class Pogrzeb(BaseModel):
    id: int
    imie: str
    nazwisko: str
    date: datetime
    parafia_id: int

class Intencja(BaseModel):
    id: int
    od_kogo: str
    kwota: float
    id_pogrzebu: int

