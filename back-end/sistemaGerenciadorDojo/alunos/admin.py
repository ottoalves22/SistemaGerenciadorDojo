from django.contrib import admin
from django.shortcuts import redirect, get_object_or_404
from django.utils.timezone import now
from django.contrib import messages
from django.urls import path

# Register your models here.
from .models import Aluno, Modalidade, Pagamento

admin.site.site_header = "Sistema Gerenciador Dojo Admin"
admin.site.site_title = "SGD Administrador"
admin.site.index_title = "Painel Administrativo"

admin.site.register(Modalidade)
admin.site.register(Pagamento)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    change_list_template = "admin/alunos/aluno/change_list.html"

    def get_urls(self):

        custom_urls = [
            path(
                "<int:aluno_id>/registrar-pagamento/",
                self.admin_site.admin_view(self.registrar_pagamento),
                name="registrar_pagamento",
            ),
        ]

        return custom_urls + super().get_urls()

    def registrar_pagamento(
        self,
        request,
        aluno_id,
    ):

        aluno = get_object_or_404(
            Aluno,
            pk=aluno_id,
        )

        Pagamento.objects.create(
            aluno=aluno,
        )

        self.message_user(
            request,
            f"Pagamento registrado para {aluno.nome}",
            messages.SUCCESS,
        )

        return redirect(f"/admin/alunos/aluno/{aluno.id}/change/")
