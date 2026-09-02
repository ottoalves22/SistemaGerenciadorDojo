#!/bin/bash
# Carrega as variáveis de ambiente do arquivo .env (gerado pelo entrypoint)
if [ -f /app/.env ]; then
    set -a
    source /app/.env
    set +a
fi

# Navega para o diretório do Django
cd /app/sistemaGerenciadorDojo

# Executa o comando
exec /app/.venv/bin/python manage.py send_monthly_fee_reminder