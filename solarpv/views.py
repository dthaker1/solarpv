from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from backend.models import Certificate, User

from solarpv.forms import RegisterForm


def register(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."

            user.save()  # Now you can send it to DB

            return HttpResponse("thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, "solarpv/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return render(request, "solarpv/login.html", {"notfound": True})
        # check whether it's valid:
        if user.usertype == "client":
            return redirect("/home/")
        elif user.usertype == "staff":
            return redirect("/admin/")

    return render(request, "solarpv/login.html")


def home(request):
    return render(request, "solarpv/home.html")


def manufacturer(request):
    return render(request, "solarpv/solarpv.html")


def certificate(request):

    if request.method == "POST":
        try:
            cert = Certificate.objects.get(certnumber=request.POST.get("search2"))
        except Certificate.DoesNotExist:
            cert = None
        if cert is not None:
            return render(request, "solarpv/certificate.html", {"cert": [cert]})
        q1 = Certificate.objects.filter(
            certnumber__icontains=request.POST.get("search2")
        )
        if len(q1) == 0:
            return render(request, "solarpv/certificate.html", {"notfound": True})
        else:
            return render(request, "solarpv/certificate.html", {"cert": q1})

    return render(request, "solarpv/certificate.html")
