# alunos/whatsapp_client.py
import os
import logging
import requests
from django.conf import settings

logger = logging.getLogger(__name__)

class WhatsAppClient:
    def __init__(self):
        self.access_token = os.getenv("WHATSAPP_ACCESS_TOKEN")
        self.phone_number_id = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
        self.api_version = os.getenv("WHATSAPP_API_VERSION", "v23.0")
        
        # Validação para falhar cedo se algo estiver faltando
        if not all([self.access_token, self.phone_number_id]):
            raise ValueError("Credenciais da API do WhatsApp não configuradas no ambiente.")
            
        self.url = (
            f"https://graph.facebook.com/{self.api_version}/"
            f"{self.phone_number_id}/messages"
        )
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def send_template_message(self, to_number: str, student_name: str):
        """
        Envia uma mensagem usando um Template aprovado pela Meta.
        Este é o método seguro para iniciar uma conversa (fora da janela de 24h).
        """
        # O nome do template deve ser EXATAMENTE o que você criou e aprovou na Meta.
        # Ex: 'lembrete_mensalidade_aluno'
        template_name = "lembrete_mensalidade_aluno" 
        
        payload = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": "pt_BR" # Código do idioma do seu template
                },
                "components": [
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": student_name # Parâmetro {{1}} do template
                            }
                        ]
                    }
                ]
            }
        }
        
        try:
            response = requests.post(
                self.url, 
                headers=self.headers, 
                json=payload, 
                timeout=30
            )
            response.raise_for_status() # Levanta exceção para erros HTTP 4xx/5xx
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao enviar template para {to_number}: {e}")
            # Trate o erro de forma específica se necessário (ex: erro 131047)
            if e.response and e.response.status_code == 400:
                error_data = e.response.json()
                if error_data.get("error", {}).get("code") == 131047:
                    logger.warning(f"Janela de 24h fechada para {to_number}. Template não pode ser enviado agora.")
            raise # Re-levanta a exceção para o comando tratar