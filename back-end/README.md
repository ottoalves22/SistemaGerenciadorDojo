# SistemaGerenciadorDojo - Projeto Integrador Grupo 15 - Univesp 2026

# Sistema Gerenciador Dojo

Sistema web desenvolvido em **Django** para gerenciamento de um dojo/academia de artes marciais. O projeto utiliza a estrutura padrão do Django para configuração do backend e gerenciamento da aplicação.

---

# 📦 Estrutura do Projeto

```
.
├── .venv/                     # Ambiente virtual Python
├── back-end/
│
├── sistemaGerenciadorDojo/    # Projeto principal Django
│   └── SGD/                   # Configurações do projeto Django
│       ├── __init__.py
│       ├── asgi.py            # Entry-point ASGI
│       ├── settings.py        # Configurações do projeto
│       ├── urls.py            # Rotas principais
│       └── wsgi.py            # Entry-point WSGI
│
├── db.sqlite3                 # Banco de dados SQLite
├── manage.py                  # CLI de gerenciamento do Django
│
├── main.py                    # Script auxiliar para execução/custom logic
│
├── pyproject.toml             # Configuração de dependências do projeto
├── uv.lock                    # Lockfile das dependências (uv)
│
├── .python-version            # Versão do Python utilizada
├── README.md                  # Documentação do projeto
└── .gitignore
```

---

# ⚙️ Tecnologias Utilizadas

* **Python**
* **Django**
* **SQLite** (banco de dados padrão)
* **uv** (gerenciamento de dependências)
* **ASGI / WSGI** para execução do servidor

---

# 🚀 Setup do Projeto

## 1. Clonar o repositório

```bash
git clone <repo-url>
cd sistemaGerenciadorDojo
```

---

## 2. Criar ambiente virtual

Caso não esteja usando o `.venv` existente:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

## 3. Instalar dependências

Se estiver utilizando **uv**:

```bash
uv sync
```

Ou via pip:

```bash
pip install -r requirements.txt
```

---

## 4. Aplicar migrations

```bash
python manage.py migrate
```

---

## 5. Criar superusuário (opcional)

```bash
python manage.py createsuperuser
```

---

## 6. Rodar o servidor

```bash
python manage.py runserver
```

Servidor disponível em:

```
http://127.0.0.1:8000
```

---

# 🗂️ Componentes Importantes

### `manage.py`

Ferramenta CLI principal do Django para executar comandos administrativos.

Exemplos:

```bash
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
```

---

### `settings.py`

Contém todas as configurações do projeto:

* Apps instaladas
* Banco de dados
* Middleware
* Configuração de segurança
* Configuração de templates

---

### `urls.py`

Define o roteamento principal da aplicação.

Exemplo:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
]
```

---

### `asgi.py` / `wsgi.py`

Arquivos de entrada para servidores de aplicação:

* **WSGI** → servidores tradicionais (gunicorn, uWSGI)
* **ASGI** → aplicações assíncronas (Daphne, Uvicorn)

---

# 🧪 Banco de Dados

O projeto utiliza **SQLite** por padrão.

Arquivo:

```
db.sqlite3
```

Para produção recomenda-se:

* PostgreSQL
* MySQL

---

# 🛠️ Desenvolvimento

Criar nova aplicação Django:

```bash
python manage.py startapp nome_da_app
```

Registrar no `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "nome_da_app",
]
```

---

# 📄 Licença

Este projeto é destinado para fins educacionais e de desenvolvimento interno.
