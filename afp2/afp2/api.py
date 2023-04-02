from ninja import NinjaAPI
from django.shortcuts import render

api = NinjaAPI()


@api.get("/test")
def hello(request):
    return render(request,'index.html')