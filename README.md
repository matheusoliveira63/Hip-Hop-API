## Hip-Hop API 🎤

Uma API RESTful simples que gerencia artistas de Hip-Hop e seus álbuns/records, desenvolvida com Flask e SQLAlchemy para fins de aprendizado em conceitos como endpoints, métodos HTTP, estrutura de dados e testes de API.

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como uma ferramenta de aprendizado para:

- Praticar desenvolvimento de APIs RESTful
- Praticar testes de API com Postman
- Entender operações CRUD básicas
- Trabalhar com Flask e SQLAlchemy

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados local

## 📋 Pré-requisitos

bash

`pip install flask flask-sqlalchemy`

## 🔧 Instalação e Execução

1. Clone ou baixe o projeto
2. Instale as dependências:

bash

`pip install flask flask-sqlalchemy`

1. Execute a aplicação:

bash

`python app.py`

1. A API estará disponível em: `http://127.0.0.1:5000`

## 📚 Endpoints da API

### 🏠 Home

`GET /`

**Resposta:**

json

`{
  "message": "Welcome to the Hip-Hop API!"
}`

### 👥 Listar Todos os Artistas

`GET /artists`

**Resposta:**

json

`[
  {
    "id": 1,
    "name": "Kendrick Lamar",
    "records": "Overly Dedicated, Section.80, good kid, m.A.A.d city, To Pimp a Butterfly, untitled unmastered., DAMN., Black Panther: The Album, Mr. Morale & The Big Steppers, GNX"
  }
]`

### 🔍 Buscar Artista por ID

`GET /artists/{id}`

**Resposta (Sucesso):**

json

`{
  "id": 1,
  "name": "Kendrick Lamar",
  "records": "Overly Dedicated, Section.80, good kid, m.A.A.d city, To Pimp a Butterfly, untitled unmastered., DAMN., Black Panther: The Album, Mr. Morale & The Big Steppers, GNX"
}`

### ➕ Criar Novo Artista

`POST /artists
Content-Type: application/json`

**Body:**

json

`{
  "name": "Lauryn Hill",
  "records": ""
}`

**Resposta:**

json

`{
  "id": 5,
  "name": "Lauryn Hill",
  "records": ""
}`

### ✏️ Atualizar Artista

`PUT /artists/{id}
Content-Type: application/json`

**Body:**

json

`{
  "name": "Lauryn Hill",
  "records": "The Miseducation of Lauryn Hill"
}`

**Resposta:**

json

`{
  "id": 5,
  "name": "Lauryn Hill",
  "records": "The Miseducation of Lauryn Hill"
}`

### 🗑️ Deletar Artista

`DELETE /artists/{id}`

**Resposta:**

json

`{
  "message": "Artist deleted successfully!"
}`

## 🧪 Testando com Postman

### Configuração Base

- **Base URL:** `http://127.0.0.1:5000`
- **Headers para POST/PUT:** `Content-Type: application/json`

### Cenários de Teste Sugeridos

### ✅ Testes Positivos

1. **GET /** - Verificar mensagem de boas-vindas
2. **GET /artists** - Listar todos os artistas
3. **POST /artists** - Criar novo artista
4. **GET /artists/{id}** - Buscar artista específico
5. **PUT /artists/{id}** - Atualizar dados do artista
6. **DELETE /artists/{id}** - Remover artista

### ❌ Testes Negativos

1. **GET /artists/999** - Buscar artista inexistente (404)
2. **PUT /artists/999** - Atualizar artista inexistente (404)
3. **DELETE /artists/999** - Deletar artista inexistente (404)
4. **POST /artists** - Enviar JSON inválido ou incompleto

### Status Codes Esperados

- **200 OK** - Operações de leitura e atualização bem-sucedidas
- **201 CREATED** - Criação de novo artista
- **404 NOT FOUND** - Artista não encontrado
- **415 UNSUPPORTED MEDIA TYPE -** Dados incompletos ou inválidos