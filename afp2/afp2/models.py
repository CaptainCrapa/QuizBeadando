from django.db import models


class Roles(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255
    )

class k_UserInRoles(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    User_Id = models.ForeignKey('RegisterUser', on_delete=models.CASCADE)
    Roles_Id = models.ForeignKey('Roles', on_delete=models.CASCADE)
class RegisterUser(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    fullname = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    username = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
        error_messages="Unique: Registration with this e-mail already exist!"
    )
    password = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    email = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
        error_messages="Unique: Registration with this e-mail already exist!"
    )
    dateOfBirth = models.DateField(
        null=True,
        blank=True
    )

class UsersLastPass(models.Model):
    id = models.AutoField(primary_key=True)
    User_Id = models.ForeignKey('RegisterUser', on_delete=models.CASCADE)
    pass_field = models.CharField(max_length=255)
    modified_at = models.DateTimeField(auto_now=True)

class UserQuiz(models.Model):
    id = models.AutoField(primary_key=True)
    User_Id = models.ForeignKey('RegisterUser', on_delete=models.CASCADE)
    Quiz_Id = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    mikor = models.DateTimeField(auto_now_add=True)
    eredmeny = models.IntegerField()

class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    Created_By = models.ForeignKey('RegisterUser', related_name='created_quizzes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_By = models.ForeignKey('RegisterUser', related_name='updated_quizzes', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

class k_QuestionInQuiz(models.Model):
    id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Question_Id = models.ForeignKey('Question', on_delete=models.CASCADE)

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255)
    answer = models.BooleanField()
    active = models.BooleanField(default=True)

class InvitedUser(models.Model):
    id = models.AutoField(primary_key=True)
    Inviter_User_Id = models.ForeignKey('RegisterUser', related_name='invited_users', on_delete=models.CASCADE)
    Invited_User_Id = models.ForeignKey('RegisterUser', related_name='inviter_users', on_delete=models.CASCADE)
    invited_at = models.DateTimeField(auto_now_add=True)
    Quiz_Id = models.ForeignKey('Quiz', on_delete=models.CASCADE)

class Meta:
    db_table = 'RegisterUser'
