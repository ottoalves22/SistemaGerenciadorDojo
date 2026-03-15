# Sistema Gerenciador Dojo

Sistema web desenvolvido em **Django** para gerenciamento de um dojo/academia de artes marciais. O projeto utiliza a estrutura padrão do Django para configuração do backend e gerenciamento da aplicação.

---

# 📦 Estrutura do Projeto

```
.
├── .venv/                     
├── back-end/                  # Diretório do backend
│
├── sistemaGerenciadorDojo/    # Projeto principal Django
│   └── SGD/                   
│       ├── __init__.py
│       ├── asgi.py            
│       ├── settings.py        
│       ├── urls.py            
│       └── wsgi.py            
│
├── db.sqlite3                 
├── manage.py                  
│
├── main.py                    
│
├── pyproject.toml             # Dependências do projeto
├── uv.lock                    # Lockfile gerado pelo uv
│
├── .python-version            
├── README.md                  
└── .gitignore
```

---

# ⚙️ Tecnologias Utilizadas

* **Python**
* **Django**
* **SQLite**
* **uv** para gerenciamento de dependências

---

# 🚀 Setup do Projeto

## 1. Clonar o repositório

```bash
git clone <repo-url>
cd sistemaGerenciadorDojo
```

---

# 📦 Gerenciamento de Dependências com UV

Este projeto utiliza **uv** para gerenciar dependências Python.

Toda a instalação deve ser feita **dentro da pasta `back-end`**.

---

## 1. Instalar o uv

Caso não tenha instalado:

Linux / Mac:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

Ou via pip:

```bash
pip install uv
```

Verifique a instalação:

```bash
uv --version
```

---

## 2. Entrar na pasta do backend

```bash
cd back-end
```

---

## 3. Instalar as dependências do projeto

```bash
uv sync
```

Esse comando irá:

* criar automaticamente um ambiente virtual
* instalar todas as dependências definidas em `pyproject.toml`
* utilizar as versões fixadas em `uv.lock`

---

## 4. Adicionar uma nova dependência

Para instalar um pacote:

```bash
uv add nome-do-pacote
```

Exemplo:

```bash
uv add django-filter
```

O `pyproject.toml` e `uv.lock` serão atualizados automaticamente.

---

## 5. Atualizar dependências

Para atualizar dependências:

```bash
uv lock --upgrade
uv sync
```

---

# ▶️ Executando o Projeto

Após instalar as dependências, ainda dentro da pasta `back-end`:

## 1. Aplicar migrations

```bash
 uv run python manage.py makemigrations {table_name}
uv run python manage.py migrate
```

---

## 2. Criar superusuário

```bash
uv run python manage.py createsuperuser
```

---

## 3. Rodar o servidor

```bash
uv run python manage.py runserver
```

Servidor disponível em:

```
http://127.0.0.1:8000
```

---

# 🗂️ Comandos Úteis

Criar migrations:

```bash
uv run python manage.py makemigrations
```

Aplicar migrations:

```bash
uv run python manage.py migrate
```

Abrir shell do Django:

```bash
uv run python manage.py shell
```

---

# 🧪 Banco de Dados

O projeto utiliza **SQLite** por padrão.

Arquivo:

```
db.sqlite3
```

Para produção recomenda-se utilizar:

* PostgreSQL
* MySQL

---

# 🛠️ Desenvolvimento

Criar uma nova aplicação Django:

```bash
uv run python manage.py startapp nome_da_app
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

Este projeto é destinado para fins educacionais e desenvolvimento acadêmico.
