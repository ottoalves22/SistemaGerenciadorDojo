from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Modalidade, Aluno, Faixa, Matricula
import datetime
from django.db import IntegrityError

class ModalidadeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.modalidade = Modalidade.objects.create(nome="Jiu-Jitsu")

    def test_nome_label(self):
        field_label = self.modalidade._meta.get_field("nome").verbose_name
        self.assertEqual(field_label, "Nome da Modalidade")

    def test_nome_max_length(self):
        max_length = self.modalidade._meta.get_field("nome").max_length
        self.assertEqual(max_length, 60)

    def test_object_name_is_nome(self):
        expected_object_name = self.modalidade.nome
        self.assertEqual(str(self.modalidade), expected_object_name)


class FaixaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        modalidade = Modalidade.objects.create(nome="Jiu-Jitsu")
        cls.faixa = Faixa.objects.create(
            nome="Branca",
            modalidade=modalidade,
            cor_faixa="Branca"
        )

    def test_nome_label(self):
        field_label = self.faixa._meta.get_field("nome").verbose_name
        self.assertEqual(field_label, "Nome da Faixa")

    def test_object_name_format(self):
        expected_object_name = f"Branca (Jiu-Jitsu)"
        self.assertEqual(str(self.faixa), expected_object_name)


class AlunoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.aluno = Aluno.objects.create(
            nome="Cabelinho",
            data_nascimento=datetime.date(1995, 5, 20),
            telefone="11999999999",
            mensalidade_em_dia=True,
            is_active=True
        )

    def test_nome_label(self):
        field_label = self.aluno._meta.get_field("nome").verbose_name
        self.assertEqual(field_label, "Nome do aluno")

    def test_object_name_is_nome(self):
        self.assertEqual(str(self.aluno), self.aluno.nome)


class MatriculaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        modalidade = Modalidade.objects.create(nome="Jiu-Jitsu")
        faixa = Faixa.objects.create(nome="Branca", modalidade=modalidade, cor_faixa="Branca")
        aluno = Aluno.objects.create(
            nome="Cabelinho",
            data_nascimento=datetime.date(1995, 5, 20),
            telefone="11999999999"
        )
        cls.matricula = Matricula.objects.create(
            aluno=aluno,
            modalidade=modalidade,
            faixa_atual=faixa,
            data_ingresso=datetime.date(2026, 1, 1)
        )

    def test_object_name_format(self):
        expected_name = f"Cabelinho - Jiu-Jitsu"
        self.assertEqual(str(self.matricula), expected_name)

    def test_unique_matricula(self):
        # Tentativa de criar matrícula duplicada deve falhar com ValidationError
        with self.assertRaises(ValidationError):
            Matricula.objects.create(
                aluno=self.matricula.aluno,
                modalidade=self.matricula.modalidade,
                data_ingresso=datetime.date(2026, 1, 2)
            )

    def test_faixa_pertence_ao_mesmo_da_modalidade(self):
        modalidade_errada = Modalidade.objects.create(nome="Krav Maga")
        faixa_errada = Faixa.objects.create(nome="Amarela", modalidade=modalidade_errada, cor_faixa="Amarela")
        with self.assertRaises(ValidationError):
            Matricula.objects.create(
                aluno=self.matricula.aluno,
                modalidade=self.matricula.modalidade,
                faixa_atual=faixa_errada,
                data_ingresso=datetime.date(2026, 1, 1)
            )
