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
    User_Id = models.ForeignKey('RegisterUser', on_delete=models.CASCADE, default=1)
    Roles_Id = models.ForeignKey('Roles', on_delete=models.CASCADE, default=1)
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


class Meta:
    db_table = 'RegisterUser'
