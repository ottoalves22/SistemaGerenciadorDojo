#!/bin/bash
# Carrega variáveis de ambiente
if [ -f /app/.env ]; then
    set -a
    source /app/.env
    set +a
fi

cd /app/sistemaGerenciadorDojo
exec /app/.venv/bin/python manage.py "$@"