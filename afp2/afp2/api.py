import json

from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from ninja import NinjaAPI, Form
from django.shortcuts import render

from afp2.schemas import RegisterUserIn, LoginUser, CreateQuizIn, CreateQuestionIn, AddQuestionToQuizIn, \
    AddUserToQuizIn, ConnectUserRoleIn, RegisterUserByAdmin, UserPasswordModification, DeleteQuiz, UnDeleteQuiz, \
    UserQuizSch, startQuiz
from afp2.models import RegisterUser, k_UserInRoles, Roles, Quiz, Question, k_QuestionInQuiz, InvitedUser, UserQuiz

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
    global glbl_quiz_id
    try:
        new_quiz = Quiz()
        new_quiz.name = data.name
        new_quiz.active = data.active
        new_quiz.Created_By = RegisterUser.objects.get(id=data.created_by)
        new_quiz.Updated_By = RegisterUser.objects.get(id=data.created_by)
        new_quiz.save()
        glbl_quiz_id = new_quiz.id
        return HttpResponse(status=201, content="Sikeresen létrehoztál egy új kvízt!")
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")


@api.post("/add_question_to_quiz")
def add_question_to_quiz(request, data: AddQuestionToQuizIn):
    question_add = k_QuestionInQuiz()
    question_add.Quiz_Id = Quiz.objects.get(id=data.quiz_id)
    question_add.Question_Id = Question.objects.get(id=data.question_id)
    try:
        question_add.save()
        return HttpResponse(status=201, content="Sikeresen hozzáadtál egy kérdést a kvízhez!")
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")


@api.post("/create_question")
def create_question(request, data: CreateQuestionIn):
    try:
        new_question = Question()
        new_question.question = data.question
        new_question.answer = data.answer
        new_question.active = data.active
        new_question.save()
        return HttpResponse(status=201, content=new_question.id)
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")


@api.post("/add_user_to_quiz")
def add_user_to_quiz(request, data: AddUserToQuizIn):
    inviter_user = RegisterUser.objects.get(id=data.inviter_user_id)
    invited_user = RegisterUser.objects.get(id=data.invited_user_id)
    quiz = Quiz.objects.get(id=data.quiz_id)
    check = InvitedUser.objects.filter(Invited_User_Id=invited_user, Quiz_Id=quiz)
    if check:
        return HttpResponse(status=403, content="Már meghívtad a felhasználót a kvízre!")
    else:
        invited_user_entry = InvitedUser(Inviter_User_Id=inviter_user, Invited_User_Id=invited_user, Quiz_Id=quiz)
        try:
            invited_user_entry.save()
            return HttpResponse(status=201, content="Sikeresen hozzáadtál egy felhasználót a Quizhez!")
        except:
            return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")


@api.post("/connect_user_role")
def connect_user_role(request, data: ConnectUserRoleIn):
    user = RegisterUser.objects.get(username=data.user_name)
    role = Roles.objects.get(id=data.role_id)
    user_in_role = k_UserInRoles.objects.get(User_id=user.id)
    user_in_role.Roles_id = role.id
    try:
        user_in_role.save()
        return HttpResponse(status=201, content="Sikeresen összekapcsoltad a felhasználót és a szerepkört!")
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")


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

@api.post("/user_quiz")
def finish_quiz(request, data: UserQuizSch):
    global glbl_quiz_id
    global glbl_user_id
    try:
        quiz_save = UserQuiz()
        quiz_save.eredmeny = data.result
        quiz_save.Quiz_Id = Quiz.objects.get(id=glbl_quiz_id)
        quiz_save.User_Id = RegisterUser.objects.get(id=glbl_user_id)
        quiz_save.save()
        return HttpResponse(status=201, content="Sikeresen lementetted a kvízt!")
    except:
        return HttpResponse(status=500, content="Adatbáziskapcsolati hiba történt!")


glbl_name = ""
glbl_user_id = 0
glbl_roles_id = 0
glbl_quiz_id = 0
glbl_quiz_list = []


@api.get("/registration")
def OpenPageReg(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id
    global glbl_quiz_list
    glbl_quiz_id = 0
    glbl_quiz_list = 0
    glbl_name = ""
    glbl_user_id = 0
    glbl_roles_id = 0
    return render(request, 'registration.html')


@api.get("/log")
def OpenPageLog(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id
    global glbl_quiz_list
    glbl_quiz_id = 0
    glbl_quiz_list = 0
    glbl_name = ""
    glbl_user_id = 0
    glbl_roles_id = 0
    return render(request, 'login.html')


@api.get("/users")
def OpenPageUser(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    return render(request, 'users.html', context)


@api.get("/menu")
def OpenPageMenu(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id
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
            'quiz_id': glbl_quiz_id,
        }
        return render(request, 'menu.html', context)


@api.get("/quiz")
def OpenPageQuiz(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    return render(request, 'quiz.html', context)


@api.get("/profile")
def OpenPageProf(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id
    if glbl_name == "":
        return render(request, 'index.html')
    else:
        user = RegisterUser.objects.get(username=glbl_name)
        fullname = user.fullname
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
            'dateOfBirth': dateOfBirth,
            'quiz_id': glbl_quiz_id,
        }
        return render(request, 'profile.html', context)


@api.get("/index")
def OpenPageIndex(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id
    global glbl_quiz_list
    glbl_quiz_id = 0
    glbl_quiz_list = 0
    glbl_name = ""
    glbl_user_id = 0
    glbl_roles_id = 0
    return render(request, 'index.html')


@api.get("/uinvite")
def OpenPageInvite(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    return render(request, 'uinvite.html', context)


@api.get("/unew")
def OpenPageNew(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    return render(request, 'unew.html', context)


@api.get("/urole")
def OpenPageRole(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    return render(request, 'urole.html', context)


@api.get("/upassword")
def OpenPagePass(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    return render(request, 'upassword.html', context)


@api.get("/qdelete")
def OpenPageDel(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    return render(request, 'qdelete.html', context)


@api.get("/qundelete")
def OpenPageUnDel(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    return render(request, 'qundelete.html', context)


@api.get("/qgenerate")
def OpenPageGen(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    return render(request, 'qgenerate.html', context)


@api.get("/qpick")
def OpenPagePick(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    return render(request, 'qpick.html', context)

@api.get("/qquestion")
def OpenPageQuestion(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'glbl_quiz_id': glbl_quiz_id,
    }
    return render(request, 'qquestion.html', context)
@api.get("/qquiz")
def OpenPageQuiz(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id
    global glbl_quiz_list

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'glbl_quiz_id': glbl_quiz_id,
        'quiz_list': json.dumps(glbl_quiz_list),
    }
    return render(request, 'qquiz.html', context)

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
            'quiz_id': glbl_quiz_id,
        }
        quiz_list.append(quiz_data)
    return HttpResponse(json.dumps(quiz_list), content_type="application/json")

@api.get("/quiz_picker")
def pick_quiz(request):
    global glbl_user_id
    invited_quizzes = InvitedUser.objects.filter(Invited_User_Id=glbl_user_id)
    quiz_ids = invited_quizzes.values_list("Quiz_Id", flat=True)
    quizzes = Quiz.objects.filter(id__in=quiz_ids)

    quiz_list = []
    for pick in quizzes:
        created_by = RegisterUser.objects.get(id=pick.Created_By_id)
        created_by_username = created_by.username

        quiz_data = {
            "id": pick.id,
            "name": pick.name,
            "active": pick.active,
            "deleted": pick.deleted,
            "Created_By_id": created_by_username,
        }
        quiz_list.append(quiz_data)
    return HttpResponse(json.dumps(quiz_list), content_type="application/json")

@api.post("/quiz_start")
def start_quiz(request, data: startQuiz):
    global glbl_quiz_id
    global glbl_quiz_list
    selected_quiz = InvitedUser.objects.get(Quiz_Id=data.quiz_id)
    question_in_connect = k_QuestionInQuiz.objects.filter(Quiz_Id=selected_quiz.Quiz_Id)
    questions = Question.objects.filter(id__in=question_in_connect.values('Question_Id'))
    glbl_quiz_id = data.quiz_id

    quiz_list = []
    for select in questions:
        quiz_data = {
            "id": select.id,
            "question": select.question,
            "answer": select.answer,
            "active": select.active,
        }
        quiz_list.append(quiz_data)

    glbl_quiz_list = quiz_list
    return HttpResponseRedirect('/api/qquiz')

@api.get("/finish_quiz")
def quiz_finish(request):
    global glbl_name
    global glbl_user_id
    global glbl_roles_id
    global glbl_quiz_id
    global glbl_quiz_list

    context = {
        'usrname': glbl_name,
        'user_id': glbl_user_id,
        'roles_id': glbl_roles_id,
        'quiz_id': glbl_quiz_id,
    }
    glbl_quiz_id = 0
    glbl_quiz_list = []
    return render(request, 'quiz.html', context)

@api.get("/get_quizzes")
def get_quizzes(request):
    global glbl_user_id

    quizzes = UserQuiz.objects.filter(User_Id=glbl_user_id).select_related('Quiz_Id')

    quiz_list = []
    for quiz in quizzes:
        quiz_data = {
            "quiz_name": quiz.Quiz_Id.name,
            "date_completed": quiz.mikor,
            "score": quiz.eredmeny,
        }
        quiz_list.append(quiz_data)

    return JsonResponse(quiz_list, safe=False)
