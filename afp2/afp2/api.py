import json

from django.db import IntegrityError
from django.http import HttpResponse
from ninja import NinjaAPI, Form
from django.shortcuts import render

from afp2.schemas import RegisterUserIn, LoginUser, CreateQuizIn, CreateQuestionIn, AddQuestionToQuizIn, \
    AddUserToQuizIn, ConnectUserRoleIn, RegisterUserByAdmin, UserPasswordModification, DeleteQuiz, UnDeleteQuiz
from afp2.models import RegisterUser, k_UserInRoles, Roles, Quiz, Question, k_QuestionInQuiz, InvitedUser

import base64

api = NinjaAPI()


@api.get("/test")
def hello(request):
    return render(request, 'index.html')


@api.post("/register")
def registerUser(request, data: RegisterUserIn):
    registerUser = RegisterUser()
    registerUser.username = data.username
    registerUser.email = data.email
    registerUser.password = base64.b64encode(data.password.encode())
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
def loginUser(request, data: LoginUser):
    global glbl_name
    registerUser = RegisterUser.objects.filter(username=data.username,
                                               password=base64.b64encode(data.password.encode())).values()
    if not registerUser:
        return HttpResponse(status=404, content="Nem található ilyen felhasználónév és jelszó párosítás!")
    else:
        glbl_name = data.username
        return HttpResponse(status=200, content="Sikeres bejelentkezés " + data.username + " felhasználóval!")


@api.post("/createUser")
def createUserByAdmin(request, data: RegisterUserByAdmin):
    try:
        admin = RegisterUser.objects.get(username=data.requester)
        role = k_UserInRoles.objects.get(User=admin)
        if role.Roles.id == 3:
            try:
                registerUser = RegisterUser()
                registerUser.username = data.username
                registerUser.email = data.email
                registerUser.password = base64.b64encode(data.password.encode())
                registerUser.fullname = data.fullname
                registerUser.dateOfBirth = data.dateOfBirth
                registerUser.save()
                roles = k_UserInRoles()
                roles.User = registerUser
                roleToSet = Roles.objects.get(name=data.role)
                roles.Roles = roleToSet
                roles.save()
                return HttpResponse(status=201, content="Sikeres regisztráció!")
            except IntegrityError:
                return HttpResponse(status=400,
                                    content="Ilyen felhasználónévvel vagy e-mail címmel már történt regisztráció!")
        else:
            return HttpResponse(status=403, content="Nincs admin jogosultságod ehhez a művelethez!")
    except:
        return HttpResponse(status=500, content="Szerver oldali hiba!")


@api.post("/modification_pw")
def modifyUserPassword(request, data: UserPasswordModification):
    try:
        admin = RegisterUser.objects.get(username=data.requester)
        role = k_UserInRoles.objects.get(User=admin)
        if role.Roles.id == 3:
            user = RegisterUser.objects.filter(username=data.username).values()
            if user:
                userForReset = RegisterUser.objects.get(username=data.username)
                userForReset.password = base64.b64encode(data.newPassword.encode())
                userForReset.save()
                return HttpResponse(status=200, content="Sikeres jelszómódosítás!")
            else:
                return HttpResponse(status=404, content="Nincs ilyen felhasználónévvel regisztrált ember!")
        else:
            return HttpResponse(status=403, content="Nincs admin jogosultságod ehhez a művelethez!")
    except:
        return HttpResponse(status=500, content="Szerver oldali hiba!")


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
    user_in_role = k_UserInRoles(User_id=user, Roles_id=role)
    try:
        user_in_role.save()
        return HttpResponse(status=201, content="Sikeresen összekapcsoltad a felhasználót és a szerepkört!")
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")


glbl_name = ""
glbl_user_id = 0
glbl_roles_id = 0


@api.get("/registration")
def OpenPageReg(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    glbl_name = ""
    glbl_user_id = 0
    glbl_roles_id = 0
    return render(request, 'registration.html')


@api.get("/log")
def OpenPageLog(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    glbl_name = ""
    glbl_user_id = 0
    glbl_roles_id = 0
    return render(request, 'login.html')


@api.get("/users")
def OpenPageUser(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
    }
    return render(request, 'users.html', context)


@api.get("/menu")
def OpenPageMenu(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    if glbl_name == "":
        return render(request, 'index.html')
    else:
        user = RegisterUser.objects.get(username=glbl_name)
        user_in_role = k_UserInRoles.objects.filter(User_id=user.id).first()
        roles_id = user_in_role.Roles_id

        glbl_user_id = user.id
        glbl_roles_id = roles_id

        context = {
            'usrname': glbl_name,
            'user_id': glbl_user_id,
            'roles_id': glbl_roles_id,
        }
        return render(request, 'menu.html', context)


@api.get("/quiz")
def OpenPageQuiz(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
    }
    return render(request, 'quiz.html', context)


@api.get("/profile")
def OpenPageProf(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    if glbl_name == "":
        return render(request, 'index.html')
    else:
        user = RegisterUser.objects.get(username=glbl_name)
        fullname = user.fullname
        # encoded_password = user.password
        # password = base64.b64decode(encoded_password).decode()
        password = user.password
        email = user.email
        dateOfBirth = user.dateOfBirth

        context = {
            'usrname': glbl_name,
            'user_id': glbl_user_id,
            'roles_id': glbl_roles_id,
            'fullname': fullname,
            'password': password,
            'email': email,
            'dateOfBirth': dateOfBirth
        }
        return render(request, 'profile.html', context)


@api.get("/index")
def OpenPageIndex(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    glbl_name = ""
    glbl_user_id = 0
    glbl_roles_id = 0
    return render(request, 'index.html')


@api.get("/uinvite")
def OpenPageInvite(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
    }
    return render(request, 'uinvite.html', context)


@api.get("/unew")
def OpenPageNew(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
    }
    return render(request, 'unew.html', context)


@api.get("/urole")
def OpenPageRole(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
    }
    return render(request, 'urole.html', context)


@api.get("/upassword")
def OpenPagePass(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
    }
    return render(request, 'upassword.html', context)


@api.get("/qdelete")
def OpenPageDel(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
    }
    return render(request, 'qdelete.html', context)


@api.get("/qundelete")
def OpenPageDel(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
    }
    return render(request, 'qundelete.html', context)


@api.get("/qgenerate")
def OpenPageGen(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
    }
    return render(request, 'qgenerate.html', context)


@api.get("/qpick")
def OpenPagePick(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
    }
    return render(request, 'qpick.html', context)


@api.post("/delete")
def DeleteQuiz(request, data: DeleteQuiz):
    role = k_UserInRoles.objects.get(User_id=data.user_id)
    if role:
        if role.Roles_id == 3:
            quiz = Quiz.objects.filter(id=data.quiz_id)
            if quiz.exists():
                try:
                    quiz.update(deleted=1)
                    return HttpResponse(status=200, content="Sikeresen törölted a quiz-t!")
                except:
                    return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")
            else:
                return HttpResponse(status=404, content="A megadott quiz nem található!")
        else:
            return HttpResponse(status=403, content="Nincs megfelelő jogosultságod a törléshez!")
    else:
        return HttpResponse(status=404, content="Nem található a felhasználó!")

@api.post("/undelete")
def UnDeleteQuiz(request, data: UnDeleteQuiz):
    role = k_UserInRoles.objects.get(User_id=data.user_id)
    if role:
        if role.Roles_id == 3:
            quiz = Quiz.objects.filter(id=data.quiz_id)
            if quiz.exists():
                try:
                    quiz.update(deleted=0)
                    return HttpResponse(status=200, content="Sikeresen visszaállítottad a kvízt!")
                except:
                    return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")
            else:
                return HttpResponse(status=404, content="A megadott quiz nem található!")
        else:
            return HttpResponse(status=403, content="Nincs megfelelő jogosultságod a visszaállításhoz!")
    else:
        return HttpResponse(status=404, content="Nem található a felhasználó!")

@api.get("/quizzes")
def list_quizzes(request):
    quizzes = Quiz.objects.all()
    quiz_list = []
    for quiz in quizzes:
        created_by = RegisterUser.objects.get(id=quiz.Created_By_id)
        updated_by = RegisterUser.objects.get(id=quiz.Updated_By_id)
        created_by_username = created_by.username
        updated_by_username = updated_by.username

        quiz_data = {
            "id": quiz.id,
            "name": quiz.name,
            "active": quiz.active,
            "created_at": quiz.created_at.isoformat(),
            "updated_at": quiz.updated_at.isoformat(),
            "deleted": quiz.deleted,
            "Created_By_id": created_by_username,
            "Updated_By_id": updated_by_username,
        }
        quiz_list.append(quiz_data)
    return HttpResponse(json.dumps(quiz_list), content_type="application/json")