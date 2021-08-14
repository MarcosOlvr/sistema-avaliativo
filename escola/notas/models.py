import abc
from django.db import models
from django.db.models.fields.related import ForeignKey
from numpy import ceil
import numpy

# Create your models here.
class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome_aluno}"

class PrimeiroBimestre(models.Model):
    primeira_nota_Português = models.FloatField()
    
    primeira_nota_Matemática = models.FloatField()
    
    primeira_nota_História = models.FloatField()
    
    primeira_nota_Geografia = models.FloatField()
    
    primeira_nota_Ciências = models.FloatField()

    primeiro_bimestre_faltas_Português = models.IntegerField()
    primeiro_bimestre_faltas_Matemática = models.IntegerField()
    primeiro_bimestre_faltas_História = models.IntegerField()
    primeiro_bimestre_faltas_Geografia = models.IntegerField()
    primeiro_bimestre_faltas_Ciências = models.IntegerField()

    def __str__(self):
        return f"Notas primeiro bimestre: {self.primeira_nota_Português} | {self.primeira_nota_Matemática} | {self.primeira_nota_História} | {self.primeira_nota_Geografia} | {self.primeira_nota_Ciências}"
    
class SegundoBimestre(models.Model):
    segunda_nota_Português = models.FloatField()
    
    segunda_nota_Matemática = models.FloatField()

    segunda_nota_História = models.FloatField()

    segunda_nota_Geografia = models.FloatField()

    segunda_nota_Ciências = models.FloatField()

    segundo_bimestre_faltas_Português = models.IntegerField()
    segundo_bimestre_faltas_Matemática = models.IntegerField()
    segundo_bimestre_faltas_História = models.IntegerField()
    segundo_bimestre_faltas_Geografia = models.IntegerField()
    segundo_bimestre_faltas_Ciências = models.IntegerField()

    def __str__(self):
        return f"Notas segundo bimestre: {self.segunda_nota_Português} | {self.segunda_nota_Matemática} | {self.segunda_nota_História} | {self.segunda_nota_Geografia} | {self.segunda_nota_Ciências}"

class TerceiroBimestre(models.Model):
    terceira_nota_Português = models.FloatField()
    
    terceira_nota_Matemática = models.FloatField()

    terceira_nota_História = models.FloatField()

    terceira_nota_Geografia = models.FloatField()

    terceira_nota_Ciências = models.FloatField()

    terceiro_bimestre_faltas_Português = models.IntegerField()
    terceiro_bimestre_faltas_Matemática = models.IntegerField()
    terceiro_bimestre_faltas_História = models.IntegerField()
    terceiro_bimestre_faltas_Geografia = models.IntegerField()
    terceiro_bimestre_faltas_Ciências = models.IntegerField()

    def __str__(self):
        return f"Notas terceiro bimestre: {self.terceira_nota_Português} | {self.terceira_nota_Matemática} | {self.terceira_nota_História} | {self.terceira_nota_Geografia} | {self.terceira_nota_Ciências}"

class QuartoBimestre(models.Model):
    quarta_nota_Português = models.FloatField()
    
    quarta_nota_Matemática = models.FloatField()

    quarta_nota_História = models.FloatField()

    quarta_nota_Geografia = models.FloatField()

    quarta_nota_Ciências = models.FloatField()

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

    def media_port(self):
        port = (self.primeiro_bimestre.primeira_nota_Português + self.segundo_bimestre.segunda_nota_Português + self.terceiro_bimestre.terceira_nota_Português + self.quarto_bimestre.quarta_nota_Português)

        return round((port)) / 4

    def media_mat(self):
        mat = (self.primeiro_bimestre.primeira_nota_Matemática + self.segundo_bimestre.segunda_nota_Matemática + self.terceiro_bimestre.terceira_nota_Matemática + self.quarto_bimestre.quarta_nota_Matemática)

        return round((mat)) / 4

    def media_hist(self):
        hist = (self.primeiro_bimestre.primeira_nota_História + self.segundo_bimestre.segunda_nota_História + self.
        terceiro_bimestre.terceira_nota_História + self.quarto_bimestre.quarta_nota_História)

        return round((hist)) / 4

    def media_geo(self):
        geo = (self.primeiro_bimestre.primeira_nota_Geografia + self.segundo_bimestre.segunda_nota_Geografia + self.terceiro_bimestre.terceira_nota_Geografia + self.quarto_bimestre.quarta_nota_Geografia)

        return round((geo)) / 4

    def media_cien(self):
        cien = (self.primeiro_bimestre.primeira_nota_Ciências + self.segundo_bimestre.segunda_nota_Ciências + self.terceiro_bimestre.terceira_nota_Ciências + self.quarto_bimestre.quarta_nota_Ciências)

        return round((cien)) / 4

    def faltas_port(self):
       return (self.primeiro_bimestre.primeiro_bimestre_faltas_Português + self.segundo_bimestre.segundo_bimestre_faltas_Português + self.terceiro_bimestre.terceiro_bimestre_faltas_Português + self.quarto_bimestre.quarto_bimestre_faltas_Português)
    
    def faltas_mat(self):
       return (self.primeiro_bimestre.primeiro_bimestre_faltas_Matemática + self.segundo_bimestre.segundo_bimestre_faltas_Matemática + self.terceiro_bimestre.terceiro_bimestre_faltas_Matemática + self.quarto_bimestre.quarto_bimestre_faltas_Matemática)
    
    def faltas_hist(self):
       return (self.primeiro_bimestre.primeiro_bimestre_faltas_História + self.segundo_bimestre.segundo_bimestre_faltas_História + self.terceiro_bimestre.terceiro_bimestre_faltas_História + self.quarto_bimestre.quarto_bimestre_faltas_História)
    
    def faltas_geo(self):
       return (self.primeiro_bimestre.primeiro_bimestre_faltas_Geografia + self.segundo_bimestre.segundo_bimestre_faltas_Geografia + self.terceiro_bimestre.terceiro_bimestre_faltas_Geografia + self.quarto_bimestre.quarto_bimestre_faltas_Geografia)
    
    def faltas_cien(self):
       return (self.primeiro_bimestre.primeiro_bimestre_faltas_Ciências + self.segundo_bimestre.segundo_bimestre_faltas_Ciências + self.terceiro_bimestre.terceiro_bimestre_faltas_Ciências + self.quarto_bimestre.quarto_bimestre_faltas_Ciências) 

    def __str__(self):
        return f"{self.aluno}"