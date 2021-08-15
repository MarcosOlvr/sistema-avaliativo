from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Final, Aluno, PrimeiroBimestre, SegundoBimestre, TerceiroBimestre, QuartoBimestre

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "notas/index.html")

def lista(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "notas/lista.html", {
        "alunos": Aluno.objects.all()
    })

def teste(request, aluno_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    aluninho = Aluno.objects.get(pk=aluno_id)
    return render(request, "notas/teste.html", {
        "aluninho": aluninho,
        "final": Final.objects.all()
    })
