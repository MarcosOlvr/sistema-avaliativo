import abc
from typing import final
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome_aluno}"

# Notas e faltas do Primeiro Bimestre
class PrimeiroBimestre(models.Model):
    primeira_nota_Português = models.FloatField(verbose_name="Nota de Língua Portuguesa")
    
    primeira_nota_Matemática = models.FloatField(verbose_name="Nota de Matemática")
    
    primeira_nota_História = models.FloatField(verbose_name="Nota de História")
    
    primeira_nota_Geografia = models.FloatField(verbose_name="Nota de Geografia")
    
    primeira_nota_Ciências = models.FloatField(verbose_name="Nota de Ciências")

    primeiro_bimestre_faltas = models.IntegerField(verbose_name="Faltas no Bimestre")

    class Meta:
        verbose_name = 'Primeiro Bimestre'
        verbose_name_plural = 'Primeiro Bimestre'

    def __str__(self):
        return f"Notas primeiro bimestre: {self.primeira_nota_Português} | {self.primeira_nota_Matemática} | {self.primeira_nota_História} | {self.primeira_nota_Geografia} | {self.primeira_nota_Ciências}"
    
# Notas e faltas do Segundo Bimestre    
class SegundoBimestre(models.Model):
    segunda_nota_Português = models.FloatField(verbose_name="Nota de Língua Portuguesa")
    
    segunda_nota_Matemática = models.FloatField(verbose_name="Nota de Matemática")

    segunda_nota_História = models.FloatField(verbose_name="Nota de História")

    segunda_nota_Geografia = models.FloatField(verbose_name="Nota de Geografia")

    segunda_nota_Ciências = models.FloatField(verbose_name="Nota de Ciências")

    segundo_bimestre_faltas = models.IntegerField(verbose_name="Faltas no Bimestre")

    class Meta:
        verbose_name = 'Segundo Bimestre'
        verbose_name_plural = 'Segundo Bimestre'

    def __str__(self):
        return f"Notas segundo bimestre: {self.segunda_nota_Português} | {self.segunda_nota_Matemática} | {self.segunda_nota_História} | {self.segunda_nota_Geografia} | {self.segunda_nota_Ciências}"

# Notas e faltas do Terceiro Bimestre
class TerceiroBimestre(models.Model):
    terceira_nota_Português = models.FloatField(verbose_name="Nota de Língua Portuguesa")
    
    terceira_nota_Matemática = models.FloatField(verbose_name="Nota de Matemática")

    terceira_nota_História = models.FloatField(verbose_name="Nota de História")

    terceira_nota_Geografia = models.FloatField(verbose_name="Nota de Geografia")

    terceira_nota_Ciências = models.FloatField(verbose_name="Nota de Ciências")

    terceiro_bimestre_faltas = models.IntegerField(verbose_name="Faltas no Bimestre")

    class Meta:
        verbose_name = 'Terceiro Bimestre'
        verbose_name_plural = 'Terceiro Bimestre'

    def __str__(self):
        return f"Notas terceiro bimestre: {self.terceira_nota_Português} | {self.terceira_nota_Matemática} | {self.terceira_nota_História} | {self.terceira_nota_Geografia} | {self.terceira_nota_Ciências}"

# Notas e faltas do Quarto Bimestre
class QuartoBimestre(models.Model):
    quarta_nota_Português = models.FloatField(verbose_name="Nota de Língua Portuguesa")
    
    quarta_nota_Matemática = models.FloatField(verbose_name="Nota de Matemática")

    quarta_nota_História = models.FloatField(verbose_name="Nota de História")

    quarta_nota_Geografia = models.FloatField(verbose_name="Nota de Geografia")

    quarta_nota_Ciências = models.FloatField(verbose_name="Nota de Ciências")

    quarto_bimestre_faltas = models.IntegerField(verbose_name="Faltas no Bimestre")

    class Meta:
        verbose_name = 'Quarto Bimestre'
        verbose_name_plural = 'Quarto Bimestre'

    def __str__(self):
        return f"Notas quarto bimestre: {self.quarta_nota_Português} | {self.quarta_nota_Matemática} | {self.quarta_nota_História} | {self.quarta_nota_Geografia} | {self.quarta_nota_Ciências}"

# Junção das notas e nome do aluno
# Calculo da média de cada matéria
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

    def delete(self):
        aluno = self.aluno
        super(Final, self).delete()
        aluno.aluno_id = Aluno.objects.filter(aluno=Aluno).count()

    class Meta:
        verbose_name = 'Adicionar notas ao aluno'
        verbose_name_plural = 'Adicionar notas ao aluno'

    def __str__(self):
        return f"{self.aluno}"