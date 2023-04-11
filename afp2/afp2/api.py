from django.db import IntegrityError
from django.http import HttpResponse
from ninja import NinjaAPI, Form
from django.shortcuts import render

from afp2.schemas import RegisterUserIn, LoginUser
from afp2.models import RegisterUser, k_UserInRoles, Roles

api = NinjaAPI()


@api.get("/test")
def hello(request):
    return render(request, 'index.html')


@api.post("/register")
def registerUser(request,data: RegisterUserIn):
        registerUser = RegisterUser()
        registerUser.username = data.username
        registerUser.email = data.email
        registerUser.password = data.password.encode()
        registerUser.fullname = data.fullname
        registerUser.dateOfBirth = data.dateOfBirth
        try:
            registerUser.save()
            roles = k_UserInRoles()
            roles.User_Id = registerUser
            roles.save()
            return HttpResponse(status=201, content="Sikeres regisztráció!")
        except IntegrityError:
            return HttpResponse(status=400, content="Ilyen felhasználónévvel vagy e-mail címmel már történt regisztráció!")
        except:
            return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")

@api.post("/login")
def loginUser(request,data: LoginUser):
    registerUser = RegisterUser.objects.filter(username=data.username, password=data.password.encode()).values()
    if not registerUser:
        return HttpResponse(status=404,content="Nem található ilyen felhasználónév és jelszó párosítás!")
    else:
        return HttpResponse(status=200,content="Sikeres bejelentkezés!")
