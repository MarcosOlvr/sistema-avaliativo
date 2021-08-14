from django.contrib import admin
from django.db.models.query_utils import Q

from .models import Final, Aluno, PrimeiroBimestre, SegundoBimestre, TerceiroBimestre, QuartoBimestre

# Register your models here.
admin.site.register(Aluno)
admin.site.register(PrimeiroBimestre)
admin.site.register(SegundoBimestre)
admin.site.register(TerceiroBimestre)
admin.site.register(QuartoBimestre)
admin.site.register(Final)
