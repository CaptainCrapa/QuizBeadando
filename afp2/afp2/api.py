from django.db import IntegrityError
from django.http import HttpResponse
from ninja import NinjaAPI, Form
from django.shortcuts import render

from afp2.schemas import RegisterUserIn, LoginUser, CreateQuizIn, CreateQuestionIn, AddQuestionToQuizIn, \
    AddUserToQuizIn, ConnectUserRoleIn, RegisterUserByAdmin, UserPasswordModification
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
            roleToSet = Roles.objects.get(id=1)
            role = k_UserInRoles()
            role.User = registerUser
            role.Roles = roleToSet
            role.save()
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
@api.post("/createUser")
def createUserByAdmin(request,data: RegisterUserByAdmin):
    try:
        admin = RegisterUser.objects.get(username=data.requester)
        role = k_UserInRoles.objects.get(User=admin)
        if role.Roles.id == 3:
            try:
                registerUser = RegisterUser()
                registerUser.username = data.username
                registerUser.email = data.email
                registerUser.password = data.password.encode()
                registerUser.fullname = data.fullname
                registerUser.dateOfBirth = data.dateOfBirth
                registerUser.save()
                roles = k_UserInRoles()
                roles.User = registerUser
                roleToSet = Roles.objects.get(id=data.role)
                roles.Roles = roleToSet
                roles.save()
                return HttpResponse(status=201, content="Sikeres regisztráció!")
            except IntegrityError:
                return HttpResponse(status=400,content="Ilyen felhasználónévvel vagy e-mail címmel már történt regisztráció!")
        else:
            return HttpResponse(status=403,content="Nincs admin jogosultságod ehhez a művelethez!")
    except:
        return HttpResponse(status=500,content="Szerver oldali hiba!")

@api.post("/modification_pw")
def modifyUserPassword(request, data: UserPasswordModification):
    try:
        admin = RegisterUser.objects.get(username=data.requester)
        role = k_UserInRoles.objects.get(User=admin)
        if role.Roles.id == 3:
            user = RegisterUser.objects.filter(username=data.username).values()
            if user:
                userForReset = RegisterUser.objects.get(username=data.username)
                userForReset.password=data.newPassword
                userForReset.save()
                return HttpResponse(status=200,content="Sikeres jelszómódosítás!")
            else:
                return HttpResponse(status=404, content="Nincs ilyen felhasználónévvel regisztrált ember!")
        else:
            return HttpResponse(status=403, content="Nincs admin jogosultságod ehhez a művelethez!")
    except:
        return HttpResponse(status=500,content="Szerver oldali hiba!")
@api.post("/create_quiz")
def create_quiz(request, data: CreateQuizIn):
    new_quiz = Quiz()
    new_quiz.name = data.name
    new_quiz.active = data.active
    new_quiz.Created_By = RegisterUser.objects.get(id=data.created_by)
    try:
        new_quiz.save()
        return HttpResponse(status=201, content="Sikeresen létrehoztál egy új Quiz-t!")
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")

@api.post("/add_question_to_quiz")
def add_question_to_quiz(request, data: AddQuestionToQuizIn):
    quiz = Quiz.objects.get(id=data.quiz_id)
    question = Question.objects.get(id=data.question_id)
    question_in_quiz = k_QuestionInQuiz(Quiz_Id=quiz, Question_Id=question)
    try:
        question_in_quiz.save()
        return HttpResponse(status=201, content="Sikeresen hozzáadtál egy kérdést a Quizhez!")
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")
@api.post("/create_question")
def create_question(request, data: CreateQuestionIn):
    new_question = Question()
    new_question.question = data.question
    new_question.answer = data.answer
    new_question.active = data.active
    try:
        new_question.save()
        return HttpResponse(status=201, content="Sikeresen létrehoztál egy új kérdést!")
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")

@api.post("/add_user_to_quiz")
def add_user_to_quiz(request, data: AddUserToQuizIn):
    inviter_user = RegisterUser.objects.get(id=data.inviter_user_id)
    invited_user = RegisterUser.objects.get(id=data.invited_user_id)
    quiz = Quiz.objects.get(id=data.quiz_id)
    invited_user_entry = InvitedUser(Inviter_User_Id=inviter_user, Invited_User_Id=invited_user, Quiz_Id=quiz)
    try:
        invited_user_entry.save()
        return HttpResponse(status=201, content="Sikeresen hozzáadtál egy felhasználót a Quizhez!")
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")

@api.post("/connect_user_role")
def connect_user_role(request, data: ConnectUserRoleIn):
    user = RegisterUser.objects.get(id=data.user_id)
    role = Roles.objects.get(id=data.role_id)
    user_in_role = k_UserInRoles(User_Id=user, Roles_Id=role)
    try:
        user_in_role.save()
        return HttpResponse(status=201, content="Sikeresen összekapcsoltad a felhasználót és a szerepkört!")
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")

@api.get("/registration")
def OpenPage(request):
    return render(request, 'registration.html')
@api.get("/users")
def OpenPage(request):
    return render(request, 'users.html')
@api.get("/users")
def OpenPage(request):
    return render(request, 'users.html')

    @api.get("/quiz")
    def OpenPage(request):
        return render(request, 'quiz.html')



        <a class="menu" href="/api/menu">Főoldal</a>
        <a class="menu" href="/api/quiz">Kvízek</a>
        <a class="menu" href="/api/profile">Profil</a>
        <a class= "menu-selected" id="users">Felhasználók</a>
        <a class="menu" href="/api/index">Kijelentkezés</a>
    </nav>
    <nav>
        <a class="menu" id="uinvite" href="/api/uinvite">Kvíz meghívó</a>
        <a class="menu" id="unew" href="/api/unew">Új felhasználó</a>
        <a class= "menu" id="urole" href="/api/urole">Szerepkör módosítás</a>
        <a class= "menu" id="upassword" href="/api/upassword">Jelszó helyreállítás</a>