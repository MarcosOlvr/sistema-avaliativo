from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("alunos", views.lista, name="lista"),
    path("<int:aluno_id>", views.teste, name="teste")
]