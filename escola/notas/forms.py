from django import forms
from .models import Aluno, Final, PrimeiroBimestre, QuartoBimestre, SegundoBimestre, TerceiroBimestre

class FinalForm(forms.ModelForm):
    class Meta:
        model = Final
        fields = ['aluno', 'primeiro_bimestre', 'segundo_bimestre', 'terceiro_bimestre', 'quarto_bimestre']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome_aluno']

class PrimeiroBiForm(forms.ModelForm):
    class Meta:
        model = PrimeiroBimestre
        fields = ['primeira_nota_Português', 'primeira_nota_Matemática', 'primeira_nota_História', 'primeira_nota_Geografia', 'primeira_nota_Ciências', 'primeiro_bimestre_faltas']

class SegundoBiForm(forms.ModelForm):
    class Meta:
        model = SegundoBimestre
        fields = ['segunda_nota_Português', 'segunda_nota_Matemática', 'segunda_nota_História', 'segunda_nota_Geografia', 'segunda_nota_Ciências', 'segundo_bimestre_faltas']

class TerceiroBiForm(forms.ModelForm):
    class Meta:
        model = TerceiroBimestre
        fields = ['terceira_nota_Português', 'terceira_nota_Matemática', 'terceira_nota_História', 'terceira_nota_Geografia', 'terceira_nota_Ciências', 'terceiro_bimestre_faltas']

class QuartoBiForm(forms.ModelForm):
    class Meta:
        model = QuartoBimestre
        fields = ['quarta_nota_Português', 'quarta_nota_Matemática', 'quarta_nota_História', 'quarta_nota_Geografia', 'quarta_nota_Ciências', 'quarto_bimestre_faltas']