from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Modalidade(models.Model):
    nome_modalidade = models.CharField(max_length=60, default="Jiu-Jitsu")


class AlunoJiu(models.Model):
    class CorFaixa(models.TextChoices):
        # Iniciante
        BRANCA = "branca", _("Branca")

        # Infantil
        CINZA_BRANCA = "cinza_branca", _("Cinza e branca")
        CINZA = "cinza", _("Cinza")
        CINZA_PRETA = "cinza_preta", _("Cinza e preta")

        AMARELA_BRANCA = "amarela_branca", _("Amarela e branca")
        AMARELA = "amarela", _("Amarela")
        AMARELA_PRETA = "amarela_preta", _("Amarela e preta")

        LARANJA_BRANCA = "laranja_branca", _("Laranja e branca")
        LARANJA = "laranja", _("Laranja")
        LARANJA_PRETA = "laranja_preta", _("Laranja e preta")

        VERDE_BRANCA = "verde_branca", _("Verde e branca")
        VERDE = "verde", _("Verde")
        VERDE_PRETA = "verde_preta", _("Verde e preta")

        # Adulto
        AZUL = "azul", _("Azul")
        ROXA = "roxa", _("Roxa")
        MARROM = "marrom", _("Marrom")
        PRETA = "preta", _("Preta")

    nome = models.CharField(max_length=60)
    data_ingresso = models.DateTimeField()
    data_nascimento = models.DateTimeField()
    cor_faixa = models.CharField(
        max_length=20, choices=CorFaixa.choices, default=CorFaixa.BRANCA
    )
    telefone = models.CharField(max_length=60)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
