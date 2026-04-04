from django.contrib import admin

# Register your models here.
from .models import Aluno, Modalidade

admin.site.site_header = "Sistema Gerenciador Dojo Admin"
admin.site.site_title = "SGD Administrador"
admin.site.index_title = "Painel Administrativo"

admin.site.register(Modalidade)
admin.site.register(Aluno)
