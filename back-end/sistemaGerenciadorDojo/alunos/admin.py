from django.contrib import admin

# Register your models here.
from .models import AlunoJiuJitsu, AlunoJudo, AlunoKravMaga, Modalidade

admin.site.register(Modalidade)
admin.site.register(AlunoJiuJitsu)
admin.site.register(AlunoJudo)
admin.site.register(AlunoKravMaga)
