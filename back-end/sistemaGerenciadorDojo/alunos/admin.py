from django.contrib import admin

# Register your models here.
from .models import Aluno, Modalidade

admin.site.register(Modalidade)
admin.site.register(Aluno)
