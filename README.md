# Gerenciador Financeiro de Terminal

Um script interativo em Python focado no controle inteligente de ganhos e gastos pessoais executado diretamente via terminal.

## Funcionalidades

### 1. Gestão de Transações (CRUD)
- **Adicionar Receitas e Despesas:** Cadastro dinâmico com geração automática de IDs.
- **Remover Itens:** Exclusão segura de registros buscando pelo ID correspondente.
- **Armazenamento Persistente:** Os dados são salvos em um arquivo `.json`, garantindo que você não perca seu histórico ao fechar o programa.

### 2. Relatórios e Interface
- **Resumo Geral:** Exibe no menu principal o total de receitas, total de despesas e o saldo líquido.
- **Interface Colorida:** O saldo líquido muda de cor dinamicamente (Verde para saldo positivo, Vermelho para negativo) usando códigos ANSI.
- **Listagem Formatada:** Apresentação limpa dos dados tabulados no terminal.

### 3. Segurança e Tratamento de Erros
- Tratamento robusto com `try/except` para evitar que o programa trave caso o usuário digite letras em campos de valor, IDs inexistentes ou deixe opções em branco.

## Tecnologias e Conceitos Utilizados
- **Python 3:** Lógica principal.
- **Bibliotecas Nativas:** `json` (para persistência de dados) e `os` (para limpeza de tela).
- **Conceitos Aplicados:** Modularização de código (separação de funções em múltiplos arquivos), Manipulação de Arquivos, Listas, Dicionários, Tratamento de Exceções e Formatação de Strings.

## Como Executar o Projeto

1. Clone este repositório ou baixe os arquivos.
2. Certifique-se de ter o Python instalado na sua máquina.
3. **Atenção:** Para testar o programa pela primeira vez, renomeie o arquivo `financeiro_exemplo.json` para `financeiro.json`.
4. Abra o terminal na pasta do projeto e execute o arquivo principal:
   ```bash
   python main.py