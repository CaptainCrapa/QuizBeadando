from datetime import date
from ninja import Schema
class RegisterUserIn(Schema):
    fullname: str
    username: str
    password: str
    email: str
    dateOfBirth: date


class LoginUser(Schema):
    username: str
    password: str


class Message(Schema):
    Message: str
