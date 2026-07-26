# 🍽️ Foodie Backend - Gerenciamento de Restaurantes

Este é o módulo principal do backend do **Foodie**, focado no gerenciamento e avaliação de restaurantes utilizando **Programação Orientada a Objetos (POO)** em Python.

---

## 🛠️ Funcionalidades Principais

*   **Cadastro Automatizado**: Armazena e organiza os restaurantes criados em uma lista centralizada da classe.
*   **Formatação de Texto**: Padroniza os nomes com a primeira letra maiúscula e as categorias em letras maiúsculas.
*   **Sistema de Status**: Exibe de forma visual se o restaurante está ativo (`☑`) ou inativo (`☐`) utilizando caracteres especiais.
*   **Sistema de Avaliações**: Permite receber notas dos clientes e calcula automaticamente a média de avaliações do estabelecimento.

---

## 📌 Pré-requisitos

Antes de iniciar, certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

*   **Python 3.13** ou superior (o projeto utiliza otimizações recentes do interpretador)
*   **Git** (para controle de versão e clonagem do repositório)

---

## 🚀 Instalação e Execução

Siga os passos abaixo para configurar o projeto localmente:

1. Clonar o repositório para a sua máquina:
   ```bash
   git clone https://github.com
   ```

2. Navegar até o diretório do projeto:
   ```bash
   cd foodie-backend-poo-py
   ```

3. Executar o arquivo principal da aplicação:
   ```bash
   python app.py
   ```

## 🗂️ Estrutura da Classe `Restaurante`

A classe demonstra a aplicação de diversos conceitos avançados de POO no Python:

### ⚙️ Métodos e Atributos de Instância
*   `__init__(nome, categoria)`: Inicializa o restaurante como inativo e aplica a formatação visual aos textos.
*   `alternar_status()`: Altera o estado atual de ativação do restaurante.
*   `receber_avaliacao(cliente, nota)`: Registra uma nova avaliação do tipo `Avaliacao`, aceitando apenas notas dentro do intervalo válido estabelecido.

### 📋 Métodos de Classe e Propriedades
*   `@classmethod listar_restaurantes()`: Percorre e exibe no terminal todos os restaurantes cadastrados em uma tabela organizada por colunas.
*   `@property ativo`: Getter que converte o status booleano interno (`True`/`False`) nos símbolos visuais de caixas de seleção.
*   `@property media_avaliacao`: Calcula de forma dinâmica a média aritmética ponderada das notas recebidas, retornando ` - ` caso ainda não existam avaliações.

---

## 🚀 Como Executar e Testar

Para testar o funcionamento desta classe, você pode instanciar novos objetos e chamar o método de listagem no seu arquivo principal (`app.py`):

```python
from models.restaurantes import Restaurante

# 1. Cadastrar restaurantes
restaurante_pizza = Restaurante('pizza planet', 'italiana')
restaurante_burger = Restaurante('burger queen', 'fast food')

# 2. Alterar status e adicionar avaliações
restaurante_pizza.alternar_status()
restaurante_pizza.receber_avaliacao('Lucca', 7)
restaurante_pizza.receber_avaliacao('Ana', 5)

# 3. Listar no terminal
Restaurante.listar_restaurantes()
```
