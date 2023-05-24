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
class RegisterUserByAdmin(Schema):
    requester: str
    fullname: str
    username: str
    password: str
    email: str
    dateOfBirth: date
    role: str
class UserPasswordModification(Schema):
    requester: str
    username: str
    newPassword: str

class Message(Schema):
    Message: str

class CreateQuizIn(Schema):
    active: bool
    name: str
    created_by: int

class CreateQuestionIn(Schema):
    question: str
    answer: bool
    active: bool

class AddQuestionToQuizIn(Schema):
    quiz_id: int
    question_id: int

class AddUserToQuizIn(Schema):
    inviter_user_id: int
    invited_user_id: int
    quiz_id: int

class ConnectUserRoleIn(Schema):
    user_id: int
    role_id: int

class DeleteQuiz(Schema):
    quiz_id: int
    user_id: int

class UnDeleteQuiz(Schema):
    quiz_id: int
    user_id: int

class startQuiz(Schema):
    quiz_id: int
