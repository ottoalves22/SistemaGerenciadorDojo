# Sistema Gerenciador do Dojo — Backend

Backend do sistema de gerenciamento do **Ornellas Dojo**, desenvolvido utilizando **Django** e executado em ambiente containerizado com **Docker**.

O sistema fornece funcionalidades administrativas para gerenciamento de alunos e outros recursos do dojo através do Django Admin customizado.

---

# Tecnologias Utilizadas

* Python 3.12
* Django
* Docker
* Docker Compose
* PostgreSQL (caso configurado no compose)
* HTML / CSS / JavaScript para customização de interface

---

# Estrutura do Projeto

```
back-end/
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── manage.py
│
├── SGD/                 # Configurações principais do projeto Django
│
├── alunos/              # App responsável pelo gerenciamento de alunos
│
├── static/              # Arquivos estáticos (CSS, JS, imagens)
│
├── templates/           # Templates HTML do sistema
│
└── README.md
```

---

# Executando o Projeto

## 1 — Clonar o repositório

```bash
git clone <repositorio>
cd back-end
```

---

## 2 — Subir os containers

```bash
docker compose up --build
```

Isso irá:

* construir a imagem do backend
* iniciar o servidor Django
* iniciar o banco de dados (se configurado)

---

## 3 — Executar migrações

Caso necessário:

```bash
docker compose exec web uv run python manage.py makemigrations
docker compose exec web uv run python manage.py migrate
```

---

## 4 — Criar superusuário

Para acessar o painel administrativo:

```bash
docker compose exec web uv run python manage.py createsuperuser
```

---

## 5 — Acessar o sistema

Aplicação:

```
http://localhost:8000
```

Painel administrativo:

```
http://localhost:8000/admin
```

---

# Django Admin Customizado

O painel administrativo foi customizado para seguir o **design do sistema do Dojo**.

Principais alterações:

* uso do CSS global do projeto
* layout compatível com o frontend
* customização de templates do admin

Principais templates sobrescritos:

```
templates/admin/base_site.html
templates/admin/index.html
templates/admin/alunos/aluno/change_list.html
templates/admin/alunos/aluno/change_form.html
```

Esses templates permitem modificar:

* dashboard do admin
* páginas de listagem
* páginas de criação e edição
* aparência geral do painel

---

# Arquivos Estáticos

Os estilos globais utilizados pelo sistema ficam em:

```
static/css/global.css
```

Esse arquivo também é carregado no **Django Admin**, permitindo que o painel administrativo siga o mesmo padrão visual do site.

---

# Desenvolvimento

Para rodar o servidor localmente sem Docker:

```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

# Aplicações do Projeto

### alunos

Responsável por:

* cadastro de alunos
* edição de dados
* gerenciamento via Django Admin

---

# Licença

Projeto desenvolvido para fins acadêmicos e administrativos do **Ornellas Dojo**.
