from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #Lista com os alunos cadastrados
    path("alunos", views.lista, name="lista"),
    #Visualizar informações do aluno
    path("alunos/<int:aluno_id>", views.aluno_nota, name="aluno_nota"),
    # Adicionar notas
    path("adicionar", views.adicionar, name="adicionar"),
    #Editar notas
    path("editar/<int:aluno_id>", views.update_nota, name="editar"),
]