# 👤 Sistema de Dados Pessoais — CLI

Um sistema simples de **cadastro e gerenciamento de dados pessoais**, desenvolvido em **Python** e executado diretamente pelo terminal.

O projeto permite cadastrar pessoas, armazenar temporariamente seus dados durante a execução do programa e visualizar todos os registros cadastrados através de um menu interativo.

> 📌 Este é o **segundo projeto** da sequência de exercícios em Python.

## 🚀 Funcionalidades

* 👤 Cadastro de novas pessoas
* 📋 Listagem de pessoas cadastradas
* 🔢 Validação da idade
* 🗃️ Armazenamento temporário dos dados
* 🖥️ Menu interativo pelo terminal
* 🧹 Limpeza automática da tela
* ❌ Tratamento de opções inválidas
* 🔄 Navegação entre diferentes funções do sistema

## 🛠️ Tecnologias

* **Python 3**
* `os`

O projeto utiliza apenas módulos da biblioteca padrão do Python, não sendo necessário instalar dependências externas.

## 📥 Instalação

Clone o repositório:

```bash
git clone https://github.com/pascalramos175/002.py.git
```

Entre na pasta:

```bash
cd 002.py
```

Execute o programa:

```bash
python main.py
```

> Caso o arquivo Python possua outro nome, substitua `main.py` pelo nome correspondente.

## 💻 Utilização

Ao executar o programa, será apresentado um menu:

```text
=================================
  SISTEMA DE DADOS PESSOAIS
=================================
1. Cadastrar nova pessoa
2. Listar pessoas cadastradas
3. Sair
=================================
Escolha uma opção (1-3):
```

### 1️⃣ Cadastrar uma pessoa

Escolha a opção `1`:

```text
=== CADASTRAR NOVA PESSOA ===

Digite o nome completo: João Silva
Digite a idade: 20
Digite o e-mail: joao@email.com
Digite o telefone (com DDD): (48) 99999-9999
```

Após o preenchimento:

```text
✅ João Silva foi cadastrado(a) com sucesso!
```

Os dados são armazenados temporariamente enquanto o programa estiver em execução.

### 2️⃣ Listar pessoas

Escolha a opção `2` para visualizar os registros:

```text
=== PESSOAS CADASTRADAS ===

[Registro #1]
  Nome: João Silva
  Idade: 20
  Email: joao@email.com
  Telefone: (48) 99999-9999
------------------------------
```

Caso nenhuma pessoa tenha sido cadastrada:

```text
Nenhum dado pessoal foi registrado ainda.
```

### 3️⃣ Sair

A opção `3` encerra o programa:

```text
Encerrando o programa. Até logo!
```

## ⚠️ Validação de idade

O sistema verifica se a idade informada é realmente um número inteiro.

Por exemplo:

```text
Digite a idade: abc
Por favor, digite um número válido para a idade.
```

O programa continuará solicitando a idade até que um número válido seja informado.

## 🗃️ Armazenamento

Os dados são armazenados em uma lista chamada:

```python
banco_de_dados = []
```

Cada pessoa cadastrada é representada por um dicionário:

```python
pessoa = {
    "Nome": nome,
    "Idade": idade,
    "Email": email,
    "Telefone": telefone
}
```

Os registros são adicionados à lista utilizando:

```python
banco_de_dados.append(pessoa)
```

### ⚠️ Armazenamento temporário

Este projeto **não utiliza um banco de dados real**.

Os registros ficam armazenados apenas na memória RAM durante a execução do programa. Ao fechar o programa, todos os dados cadastrados são perdidos.

## 🧹 Limpeza do terminal

O projeto utiliza o módulo `os` para limpar o terminal antes de exibir cada tela:

```python
os.system('cls' if os.name == 'nt' else 'clear')
```

Dessa forma, o comando utilizado depende do sistema operacional:

* **Windows:** `cls`
* **Linux/macOS:** `clear`

## 📂 Estrutura do projeto

```text
002.py/
│
├── main.py
└── README.md
```

## 🧠 Conceitos praticados

Este projeto foi desenvolvido para praticar conceitos fundamentais de Python, incluindo:

* Variáveis
* Listas
* Dicionários
* Funções
* `input()`
* `print()`
* Estruturas condicionais
* Loops `while`
* Loops `for`
* `try/except`
* Manipulação de strings
* Módulos
* `os.system()`
* Estruturas de dados
* Organização de aplicações via terminal

## 🎯 Objetivo

O objetivo deste projeto é praticar a criação de uma aplicação interativa em Python utilizando estruturas básicas da linguagem.

O projeto também serve como uma introdução a conceitos que podem posteriormente ser utilizados em sistemas mais complexos, como:

* Sistemas de cadastro
* APIs
* Bancos de dados
* Sistemas CRUD
* Aplicações web
* Sistemas de gerenciamento

## 📚 Próximos passos

Algumas melhorias que poderiam ser implementadas futuramente:

* 💾 Persistência dos dados em arquivo JSON
* 🗄️ Utilização de SQLite
* ✏️ Edição de pessoas cadastradas
* 🗑️ Exclusão de registros
* 🔎 Busca por nome ou e-mail
* 📧 Validação de e-mail
* 📱 Formatação e validação de telefone
* 🔐 Sistema de autenticação
* 🖥️ Interface gráfica

## 👨‍💻 Autor

**Pascal Ramos**

GitHub: [@pascalramos175](https://github.com/pascalramos175)

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!
