# 📚 API de Cadastramento de Livros

API simples para cadastro e gerenciamento de livros, desenvolvida em Python utilizando Flask e SQLite.

---

## 🚀 Funcionalidades

* 📌 Cadastrar um livro
* 📌 Listar todos os livros cadastrados
* 📌 Buscar um livro pelo ID
* 📌 Deletar um livro pelo ID

---

## ⚙️ Como executar a API

### 1. Instalar as dependências

No terminal, execute:

```
pip install -r requirements.txt
```

### 2. Iniciar a aplicação

Tente primeiro:

```
flask run
```

Caso não funcione:

```
python biblioteca.py
```

No Linux:

```
python3 biblioteca.py
```

---

## 🧪 Testando a API

Para testar os endpoints, utilize o **Postman** (ou outra ferramenta similar).

### Exemplo de requisição (JSON)

```json
{
  "nome": "Nome do Livro",
  "autor": "Autor do Livro",
  "preco": 99.99,
  "ano": 2026,
  "data_retirada": "2025-04-14",
  "data_entrega": "2026-05-03"
}
```

⚠️ **Observações importantes:**

* As datas devem estar no formato `YYYY-MM-DD` ou 'YYYY/MM/DD'
* Os campos devem ser preenchidos corretamente

---

## 🔗 Rotas da API

### 📌 Testar conexão da API

* **GET** `/test`
  Retorna uma mensagem confirmando que a API está funcionando.

**Resposta:**

```json
{
  "msg": "Api conectada"
}
```

---

### 📌 Cadastrar um novo livro

* **POST** `/livros`

**Body (JSON):**

```json
{
  "nome": "Nome do Livro",
  "autor": "Autor do Livro",
  "preco": 99.99,
  "ano": 2026,
  "data_retirada": "2025-04-14",
  "data_entrega": "2026-05-03"
}
```

**Respostas possíveis:**

* `201` → Livro cadastrado com sucesso
* `400` → Dados inválidos (campos vazios, datas inválidas, valores negativos)
* `500` → Erro interno ao cadastrar

---

### 📌 Listar todos os livros

* **GET** `/livros`

**Respostas:**

* `200` → Lista de livros
* `404` → Nenhum livro cadastrado

---

### 📌 Buscar livro por ID

* **GET** `/livros/<id>`

**Exemplo:**

```
/livros/1
```

**Respostas:**

* `200` → Livro encontrado
* `404` → Livro não encontrado

---

### 📌 Deletar livro por ID

* **DELETE** `/livros/<id>`

**Exemplo:**

```
/livros/1
```

**Respostas:**

* `200` → Livro deletado com sucesso
* `404` → Livro não encontrado

---

## ✅ Validações implementadas

* ❌ Não permite valores negativos (ex: preço)
* ❌ Não permite campos vazios
* ❌ Valida datas:

  * A data de retirada não pode ser maior que a data de entrega

---

## 🛠️ Tecnologias utilizadas

* Flask (framework web em Python)
* SQLite3 (banco de dados)
* Datetime (manipulação de datas)

---

## 📌 Observações

Esta API foi desenvolvida com foco educacional, para prática de conceitos como:

* Métodos HTTP (GET, POST, DELETE)
* Estrutura de APIs REST
* Validação de dados
* Integração com banco de dados

---
