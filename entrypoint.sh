#!/bin/bash
set -e

# Gera .env com as variáveis necessárias
printenv | grep -E '^(DJANGO_|POSTGRES_|DATABASE_)' > /app/.env

# Instala cron (se não estiver)
apt-get update -qq && apt-get install -y -qq cron > /dev/null

# Cria arquivo de log e dá permissão
touch /var/log/django_cron.log
chmod 666 /var/log/django_cron.log

# Adiciona os jobs ao crontab
cd /app/sistemaGerenciadorDojo

# >>> CORREÇÃO AQUI: Usa `uv run python` para pegar a venv automaticamente <<<
uv run python /app/sistemaGerenciadorDojo/manage.py collectstatic --noinput

# >>> CORREÇÃO AQUI: Usa `uv run python` para o crontab (mantendo a consistência) <<<
uv run python manage.py crontab add

# Inicia o cron em background
service cron start

# Executa o comando principal do container
exec "$@"