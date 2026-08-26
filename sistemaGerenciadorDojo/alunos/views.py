from django.shortcuts import render
from .models import Aluno, Modalidade  # ajuste conforme seus models

def index(request):
    alunos = Aluno.objects.all()
    modalidades = Modalidade.objects.all()
    return render(request, "alunos/alunos.html", {
        "alunos": alunos,
        "modalidades": modalidades,
    })