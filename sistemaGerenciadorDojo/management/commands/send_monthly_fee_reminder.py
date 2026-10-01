from django.core.management.base import BaseCommand
from alunos.models import Aluno
from alunos.whatsapp_client import WhatsAppClient
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Envia lembretes de cobrança da mensalidade pelo WhatsApp usando templates."

    """
    def handle(self, *args, **options):
        try:
            client = WhatsAppClient()
        except ValueError as e:
            self.stderr.write(self.style.ERROR(str(e)))
            return

        # É uma boa prática filtrar alunos que possuem um número de WhatsApp
        alunos = Aluno.objects.exclude(whatsapp__isnull=True).exclude(whatsapp__exact='')
        # alunos = Aluno.objects.all() # Ou como você preferir

        for aluno in alunos:
            try:
                # O número de telefone deve estar no formato internacional (ex: +5511999999999)
                # Certifique-se de que seu campo 'whatsapp' esteja limpo e validado.
                numero_limpo = self._limpar_numero(aluno.whatsapp)
                if not numero_limpo:
                    logger.warning(f"Número de WhatsApp inválido para o aluno {aluno.nome}. Pulando.")
                    continue

                # Chama o método seguro do nosso cliente
                response = client.send_template_message(
                    to_number=numero_limpo,
                    student_name=aluno.nome
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Lembrete enviado para {aluno.nome} (ID: {response.get('messages', [{}])[0].get('id')})")
                )
            except Exception as e:
                self.stderr.write(
                    self.style.ERROR(f"Falha ao enviar para {aluno.nome}: {e}")
                )
            finally:
                # É crucial pausar entre as requisições para evitar bloqueios ou limitação de taxa (rate limiting).
                # 1 a 2 segundos é um valor seguro para começar.
                import time
                time.sleep(1.5) 

    def _limpar_numero(self, numero: str) -> str:
        if not numero:
            return ""
        # Remove tudo que não for dígito
        numeros = ''.join(filter(str.isdigit, numero))
        # A API da Meta requer o código do país. Ajuste conforme necessário.
        # Se o seu número já tem o código do país (ex: 55 para Brasil), adicione '+' na frente.
        # Este é um exemplo simples; o ideal é ter uma biblioteca como 'phonenumbers' para isso.
        return f"+{numeros}"
    """
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
