from src.database import UsersDB
from passlib.context import CryptContext

from src.models import UserInDB
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

username = input("username: ")
password = input("password: ")

UsersDB().add(data=UserInDB(username=username, hashed_password=pwd_context.hash(password)))
print("Done!")