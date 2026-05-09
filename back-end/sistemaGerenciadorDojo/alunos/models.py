from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class Modalidade(models.Model):
    nome = models.CharField(
        max_length=60, default="Jiu-Jitsu", verbose_name=_("Nome da Modalidade")
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "modalidade"


class Aluno(models.Model):
    class Faixa(models.TextChoices):
        BRANCA = "branca", "Branca"
        AZUL = "azul", "Azul"
        ROXA = "roxa", "Roxa"
        MARROM = "marrom", "Marrom"
        PRETA = "preta", "Preta"

        # Kids (infantil)
        CINZA = "cinza", "Cinza"
        AMARELA = "amarela", "Amarela"
        LARANJA = "laranja", "Laranja"
        VERDE = "verde", "Verde"

    nome = models.CharField(max_length=60, verbose_name=_("Nome do aluno"))
    modalidade = models.ForeignKey(
        Modalidade, on_delete=models.CASCADE, related_name="alunos", default=None
    )
    faixa = models.CharField(
        max_length=10,
        choices=Faixa.choices,
        default=Faixa.BRANCA,
        verbose_name=_("Cor da Faixa"),
    )
    data_nascimento = models.DateField(verbose_name=_("Data de Nascimento"))
    cpf = models.CharField(max_length=60, verbose_name=_("CPF"))
    telefone = models.CharField(max_length=60, verbose_name=_("Telefone"))
    contato_emergencia = models.CharField(
        max_length=60,
        verbose_name=_("Contato de Emergência"),
        default="",
        null=True,
        blank=True,
    )
    aluno_ativo = models.BooleanField(default=True, verbose_name=_("Ativo"))
    mensalidade_em_dia = models.BooleanField(
        default=False, verbose_name=_("Mensalidade em Dia")
    )  # Já começa devendo

    def __str__(self):
        return f"{self.nome}-{self.modalidade}"

    class Meta:
        db_table = "aluno"


class Pagamento(models.Model):

    aluno = models.ForeignKey(
        "Aluno",
        on_delete=models.CASCADE,
        related_name="pagamentos",
    )

    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=280.00,
    )

    data_pagamento = models.DateTimeField(
        auto_now_add=True,
    )

    mes_referencia = models.DateField(
        default=now,
    )

    class Meta:
        db_table = "pagamento"

    def __str__(self):
        return f"{self.aluno.nome} - " f"{self.mes_referencia.strftime('%m/%Y')}"
