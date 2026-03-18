from django.db import models
from django.utils.translation import gettext_lazy as _


class Modalidade(models.Model):
    nome = models.CharField(max_length=60, default="Jiu-Jitsu", verbose_name=_("Nome da Modalidade"))

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'modalidade'

class Faixa(models.Model):
    nome = models.CharField(max_length=50, verbose_name=_("Nome da Faixa"))
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, related_name='faixas', verbose_name=_("Modalidade"))

    def __str__(self):
        return f"{self.nome} ({self.modalidade.nome})"

    class Meta:
        db_table = 'faixa'


class Aluno(models.Model):
    nome = models.CharField(max_length=60, verbose_name=_("Nome do aluno"))
    data_nascimento = models.DateField(verbose_name=_("Data de Nascimento"))
    telefone = models.CharField(max_length=60, verbose_name=_("Telefone"))
    mensalidade_em_dia = models.BooleanField(default=False, verbose_name=_("Mensalidade em Dia")) # Já começa devendo
    is_active = models.BooleanField(default=True, verbose_name=_("Ativo"))

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'aluno'

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas', verbose_name=_("Aluno"))
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, related_name='matriculas', verbose_name=_("Modalidade"))
    faixa_atual = models.ForeignKey(Faixa, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Faixa Atual"))
    data_ingresso = models.DateField(verbose_name=_("Data de Ingresso"))

    def __str__(self):
        return f"{self.aluno.nome} - {self.modalidade.nome}"

    class Meta:
        db_table = 'matriculas'
        unique_together = ('aluno', 'modalidade')
