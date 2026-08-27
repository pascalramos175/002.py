# 👋 Saudação Personalizada — Python

Um programa simples em **Python** que solicita o nome do usuário e exibe uma saudação personalizada.

## 📌 Sobre o projeto

Este projeto demonstra como receber informações digitadas pelo usuário através do terminal e utilizá-las para criar uma mensagem personalizada.

O programa pergunta o nome do usuário e, em seguida, exibe uma saudação utilizando o nome informado.

## 💻 Código

```python
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
```

## 🔎 Como funciona?

### `input()`

A função `input()` permite receber uma informação digitada pelo usuário.

```python
nome = input("Qual é o seu nome? ")
```

Nesse caso:

* `"Qual é o seu nome? "` é a pergunta exibida no terminal.
* O usuário digita seu nome.
* O valor digitado é armazenado na variável `nome`.

### `print()`

A função `print()` exibe uma mensagem no terminal:

```python
print(f"Olá, {nome}!")
```

O `f` antes das aspas indica uma **f-string**, permitindo inserir o valor de uma variável diretamente dentro do texto utilizando `{}`.

## ▶️ Exemplo de execução

```text
Qual é o seu nome? Pascal
Olá, Pascal!
```

## 📚 Conceitos aprendidos

| Conceito  | Descrição                                  |
| --------- | ------------------------------------------ |
| `input()` | Recebe dados digitados pelo usuário        |
| Variáveis | Armazenam informações durante a execução   |
| `print()` | Exibe informações no terminal              |
| f-string  | Permite inserir variáveis dentro de textos |
| Strings   | Representam textos em Python               |

## 🎯 Objetivo

Este projeto foi desenvolvido para praticar **entrada e saída de dados**, variáveis e formatação de strings em Python.

É um pequeno passo para começar a criar programas interativos.

---

🐍 **Python — Projeto de Introdução**
