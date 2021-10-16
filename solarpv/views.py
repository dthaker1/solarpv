from django.http.response import HttpResponse
from django.shortcuts import render


def register(request):
    return render(request, "solarpv/register.html")


def home(request):
    return render(request, "solarpv/home.html")


def manufacturer(request):
    return render(request, "solarpv/solarpv.html")
