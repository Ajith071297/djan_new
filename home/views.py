from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    view_user=[
    {"name":"selva","age":23},
    {"name":"Ajith","age":26},
    {"name":"selva","age":23},
    {"name":"kumar","age":13},
    ]

    return render(request, "index.html",context={"users":view_user})

