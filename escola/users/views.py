from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "notas/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        senha = request.POST["senha"]
        user = authenticate(request, username = username, senha = senha)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))   
        else:
            return render(request, "users/login.html", {
                "mensagem": 'Credenciais inválidas'
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "mensagem":"Logged out"
    })