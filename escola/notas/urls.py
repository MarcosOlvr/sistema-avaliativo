from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("alunos", views.lista, name="lista"),
    path("<int:aluno_id>", views.aluno_nota, name="aluno_nota"),
    # Adicionar notas
    path("adicionar", views.adicionar, name="adicionar"),
]