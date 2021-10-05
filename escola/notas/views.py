from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import FinalForm, AlunoForm, PrimeiroBiForm, SegundoBiForm, TerceiroBiForm, QuartoBiForm

from .models import Final, Aluno, PrimeiroBimestre, SegundoBimestre, TerceiroBimestre, QuartoBimestre

# Create your views here.
def index(request):
    return render(request, "notas/index.html")

def lista(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "notas/lista.html", {
        "alunos": Aluno.objects.all()
    })

def aluno_nota(request, aluno_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    aluninho = Aluno.objects.get(pk=aluno_id)

    if request.method == 'POST':
        final_aluno = Aluno.objects.get(pk=aluno_id)
        final_bi1 = PrimeiroBimestre.objects.get(pk=aluno_id)
        final_bi2 = SegundoBimestre.objects.get(pk=aluno_id)
        final_bi3 = TerceiroBimestre.objects.get(pk=aluno_id)
        final_bi4 = QuartoBimestre.objects.get(pk=aluno_id)
        final_aluno.delete()
        final_bi1.delete()
        final_bi2.delete()
        final_bi3.delete()
        final_bi4.delete()
        return redirect("lista")

    return render(request, "notas/aluno_nota.html", {
        "aluninho": aluninho,
        "final": Final.objects.all()
    })

def adicionar(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.method == 'POST':
        aluno = Aluno()
        aluno.nome_aluno = request.POST.get("nome_aluno")
        if aluno.nome_aluno is not None:
            #salvando NOTAS do PRIMEIRO bimestre
            aluno.save()
            bi1 = PrimeiroBimestre()
            bi1.primeira_nota_Português = request.POST.get("bi1_nota_port")
            bi1.primeira_nota_Matemática = request.POST.get("bi1_nota_mat")
            bi1.primeira_nota_História = request.POST.get("bi1_nota_hist")
            bi1.primeira_nota_Geografia = request.POST.get("bi1_nota_geo")
            bi1.primeira_nota_Ciências = request.POST.get("bi1_nota_cien")
            #salvando FALTAS do PRIMEIRO bimestre
            bi1.primeiro_bimestre_faltas = request.POST.get("bi1_faltas")
            bi1.save()

            #salvando NOTAS do SEGUNDO bimestre
            bi2 = SegundoBimestre()
            bi2.segunda_nota_Português = request.POST.get("bi2_nota_port")
            bi2.segunda_nota_Matemática = request.POST.get("bi2_nota_mat")
            bi2.segunda_nota_História = request.POST.get("bi2_nota_hist")
            bi2.segunda_nota_Geografia = request.POST.get("bi2_nota_geo")
            bi2.segunda_nota_Ciências = request.POST.get("bi2_nota_geo")
            #salvando FALTAS do SEGUNDO bimestre
            bi2.segundo_bimestre_faltas = request.POST.get("bi2_faltas")
            bi2.save()

            #salvando NOTAS do TERCEIRO bimestre
            bi3 = TerceiroBimestre()
            bi3.terceira_nota_Português = request.POST.get("bi3_nota_port")
            bi3.terceira_nota_Matemática = request.POST.get("bi3_nota_mat")
            bi3.terceira_nota_História = request.POST.get("bi3_nota_hist")
            bi3.terceira_nota_Geografia = request.POST.get("bi3_nota_geo")
            bi3.terceira_nota_Ciências = request.POST.get("bi3_nota_geo")
            #salvando FALTAS do TERCEIRO bimestre
            bi3.terceiro_bimestre_faltas = request.POST.get("bi3_faltas")
            bi3.save()

            #salvando NOTAS do QUARTO bimestre
            bi4 = QuartoBimestre()
            bi4.quarta_nota_Português = request.POST.get("bi4_nota_port")
            bi4.quarta_nota_Matemática = request.POST.get("bi4_nota_mat")
            bi4.quarta_nota_História = request.POST.get("bi4_nota_hist")
            bi4.quarta_nota_Geografia = request.POST.get("bi4_nota_geo")
            bi4.quarta_nota_Ciências = request.POST.get("bi4_nota_geo")
            #salvando FALTAS do QUARTO bimestre
            bi4.quarto_bimestre_faltas = request.POST.get("bi4_faltas")
            bi4.save()

            #adicionando na tabela
            f = Final()
            f.aluno = aluno
            f.primeiro_bimestre = bi1
            f.segundo_bimestre = bi2
            f.terceiro_bimestre = bi3
            f.quarto_bimestre = bi4
            f.save()

            return redirect("lista")
    
    return render(request, "notas/adicionar.html")

def update_nota(request, aluno_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    aluno = Aluno.objects.get(pk=aluno_id)
    primeiro = PrimeiroBimestre.objects.get(pk=aluno_id)
    segundo = SegundoBimestre.objects.get(pk=aluno_id)
    terceiro = TerceiroBimestre.objects.get(pk=aluno_id)
    quarto = QuartoBimestre.objects.get(pk=aluno_id)
    
    form_aluno = AlunoForm(request.POST or None, instance=aluno)
    form_primeiro = PrimeiroBiForm(request.POST or None, instance=primeiro)
    form_segundo = SegundoBiForm(request.POST or None, instance=segundo)
    form_terceiro = TerceiroBiForm(request.POST or None, instance=terceiro)
    form_quarto = QuartoBiForm(request.POST or None, instance=quarto)

    if form_aluno.is_valid():
        form_aluno.save()
    
    if form_primeiro.is_valid():
        form_primeiro.save()
    
    if form_segundo.is_valid():
        form_segundo.save()
    
    if form_terceiro.is_valid():
        form_terceiro.save()
    
    if form_quarto.is_valid():
        form_quarto.save()
        return redirect("lista")
    
    return render(request, 'notas/editar_nota.html',{
        'form_aluno':form_aluno, 
        'form_primeiro':form_primeiro,
        'form_segundo':form_segundo,
        'form_terceiro':form_terceiro,
        'form_quarto':form_quarto,
        'aluno':aluno
    })