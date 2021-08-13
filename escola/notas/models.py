import abc
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome_aluno}"

class PrimeiroBimestre(models.Model):
    primeira_nota_Português = models.IntegerField()
    
    primeira_nota_Matemática = models.IntegerField()
    
    primeira_nota_História = models.IntegerField()
    
    primeira_nota_Geografia = models.IntegerField()
    
    primeira_nota_Ciências = models.IntegerField()

    primeiro_bimestre_faltas_Português = models.IntegerField()
    primeiro_bimestre_faltas_Matemática = models.IntegerField()
    primeiro_bimestre_faltas_História = models.IntegerField()
    primeiro_bimestre_faltas_Geografia = models.IntegerField()
    primeiro_bimestre_faltas_Ciências = models.IntegerField()

    def __str__(self):
        return f"Notas primeiro bimestre: {self.primeira_nota_Português} | {self.primeira_nota_Matemática} | {self.primeira_nota_História} | {self.primeira_nota_Geografia} | {self.primeira_nota_Ciências}"
    
class SegundoBimestre(models.Model):
    segunda_nota_Português = models.IntegerField()
    
    segunda_nota_Matemática = models.IntegerField()

    segunda_nota_História = models.IntegerField()

    segunda_nota_Geografia = models.IntegerField()

    segunda_nota_Ciências = models.IntegerField()

    segundo_bimestre_faltas_Português = models.IntegerField()
    segundo_bimestre_faltas_Matemática = models.IntegerField()
    segundo_bimestre_faltas_História = models.IntegerField()
    segundo_bimestre_faltas_Geografia = models.IntegerField()
    segundo_bimestre_faltas_Ciências = models.IntegerField()

    def __str__(self):
        return f"Notas segundo bimestre: {self.segunda_nota_Português} | {self.segunda_nota_Matemática} | {self.segunda_nota_História} | {self.segunda_nota_Geografia} | {self.segunda_nota_Ciências}"

class TerceiroBimestre(models.Model):
    terceira_nota_Português = models.IntegerField()
    
    terceira_nota_Matemática = models.IntegerField()

    terceira_nota_História = models.IntegerField()

    terceira_nota_Geografia = models.IntegerField()

    terceira_nota_Ciências = models.IntegerField()

    terceiro_bimestre_faltas_Português = models.IntegerField()
    terceiro_bimestre_faltas_Matemática = models.IntegerField()
    terceiro_bimestre_faltas_História = models.IntegerField()
    terceiro_bimestre_faltas_Geografia = models.IntegerField()
    terceiro_bimestre_faltas_Ciências = models.IntegerField()

    def __str__(self):
        return f"Notas terceiro bimestre: {self.terceira_nota_Português} | {self.terceira_nota_Matemática} | {self.terceira_nota_História} | {self.terceira_nota_Geografia} | {self.terceira_nota_Ciências}"

class QuartoBimestre(models.Model):
    quarta_nota_Português = models.IntegerField()
    
    quarta_nota_Matemática = models.IntegerField()

    quarta_nota_História = models.IntegerField()

    quarta_nota_Geografia = models.IntegerField()

    quarta_nota_Ciências = models.IntegerField()

    quarto_bimestre_faltas_Português = models.IntegerField()
    quarto_bimestre_faltas_Matemática = models.IntegerField()
    quarto_bimestre_faltas_História = models.IntegerField()
    quarto_bimestre_faltas_Geografia = models.IntegerField()
    quarto_bimestre_faltas_Ciências = models.IntegerField()

    def __str__(self):
        return f"Notas quarto bimestre: {self.quarta_nota_Português} | {self.quarta_nota_Matemática} | {self.quarta_nota_História} | {self.quarta_nota_Geografia} | {self.quarta_nota_Ciências}"

class Final(models.Model):
    aluno = ForeignKey(Aluno, on_delete=models.CASCADE, related_name="aluno")

    primeiro_bimestre = ForeignKey(PrimeiroBimestre, on_delete=models.CASCADE, related_name="primeiro_bimestre")

    segundo_bimestre = ForeignKey(SegundoBimestre, on_delete=models.CASCADE, related_name="segundo_bimestre")

    terceiro_bimestre = ForeignKey(TerceiroBimestre, on_delete=models.CASCADE, related_name="terceiro_bimestre")

    quarto_bimestre = ForeignKey(QuartoBimestre, on_delete=models.CASCADE, related_name="quarto_bimestre")

    def __str__(self):
        return f"{self.aluno}"