# Sistema Gerenciador Dojo - P.I Grupo 15 - Univesp 2026

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

O projeto utiliza **PostgreSQL** como banco de dados principal, gerenciado via **Docker Compose** para facilitar o ambiente de desenvolvimento.

Para rodar o banco de dados, você precisará do Docker e do Docker Compose instalados.

### Instalação

1. **Instalar Docker e Docker Compose V2**:
   Usar a documentação oficial do Docker para instalar o Docker e o Docker Compose V2.
   [text](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

2. **Verificar instalação**:
   ```bash
   docker --version
   docker compose version
   ```

---

## 🚀 Rodando o PostgreSQL

Toda a configuração do banco de dados está no arquivo `back-end/docker-compose.yml`.

### 1. Subir o container

Dentro da pasta `back-end`, execute:

```bash
docker-compose up -d
```

O container será baixado e executado em segundo plano.

### 2. Credenciais de Acesso

As credenciais configuradas no `docker-compose.yml` e `settings.py` são:

* **DB Name**: `sgd_db`
* **User**: `sgd_user`
* **Password**: `sgd_password`
* **Port**: `5432`

### 3. Verificar se o banco está rodando

```bash
docker ps
```

Você deverá ver o container `sgd_postgres` na lista.

---

### Migrations

Após subir o banco pela primeira vez, não esqueça de aplicar as migrations:

```bash
cd back-end
uv run python manage.py migrate
```

---

# 🧪 Executando os Testes

Para garantir a integridade do sistema, você pode executar a suíte de testes automatizados. 

Dentro da pasta `back-end/sistemaGerenciadorDojo`, execute:

```bash
python manage.py test alunos
```

Ou, caso prefira usar o `uv`:

```bash
uv run python manage.py test alunos
```

### O que é testado?
* **Modelos**: Validação de rótulos (labels), comprimentos máximos e nomes de exibição (`__str__`).
* **Regras de Negócio**: 
    * Unicidade de matrículas (um aluno não pode ter duas matrículas na mesma modalidade).
    * Consistência de faixas (um aluno só pode ser matriculado em uma faixa que pertença à modalidade escolhida).

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
