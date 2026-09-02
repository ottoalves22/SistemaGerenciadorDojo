from django.core.management.base import BaseCommand
from alunos.models import Aluno  # Assumindo que você usa o Aluno padrão

# from seu_app.models import Aluno  # ou seu modelo de aluno

# Importe aqui a sua função de envio de WhatsApp
# from seu_app.whatsapp import send_whatsapp_message


class Command(BaseCommand):
    help = "Envia lembretes de cobrança da mensalidade pelo WhatsApp"

    def handle(self, *args, **options):
        # 1. Buscar todos os alunos que têm um número de WhatsApp cadastrado
        # alunos = Aluno.objects.filter(whatsapp__isnull=False)
        alunos = Aluno.objects.all()  # Exemplo: pegando todos os usuários

        for aluno in alunos:
            # 2. Para cada aluno, montar a mensagem personalizada
            mensagem = f"Olá {aluno.nome}, sua mensalidade do Ornellas Dojo vence em breve. Acesse o sistema para mais informações."

            # 3. Enviar a mensagem via WhatsApp
            # send_whatsapp_message(aluno.whatsapp, mensagem)
            self.stdout.write(self.style.SUCCESS(f"Mensagem enviada para {aluno.nome}"))
