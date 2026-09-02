FROM python:3.12-slim

WORKDIR /app


# Copia arquivos de requisitos
COPY pyproject.toml uv.lock* ./

# Instala uv e dependências
RUN pip install uv && uv sync --frozen

# Copia o código
COPY . .

# Torna scripts executáveis
RUN chmod +x entrypoint.sh cron_command.sh

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "SGD.wsgi"]