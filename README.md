# Sistema Bancário Simples

Este é um projeto acadêmico de um sistema bancário simples desenvolvido em Python. O sistema permite realizar operações básicas de depósito, saque e visualização de extrato.

## Funcionalidades

- **Depósito:** Permite ao usuário depositar valores em sua conta.
- **Saque:** Permite ao usuário sacar valores de sua conta, com um limite máximo de R$500,00 por operação.
- **Extrato:** Exibe todas as transações realizadas e o saldo atual da conta.

## Como Usar

1. **Pré-requisitos:** Certifique-se de ter o Python instalado em sua máquina.

2. **Execução:**
   - Clone este repositório ou baixe o arquivo do sistema bancário.
   - Navegue até o diretório do projeto.
   - Execute o script Python usando o comando:
     ```bash
     python main.py
     ```

3. **Menu de Opções:**
   - Escolha uma das opções do menu para realizar operações bancárias.
   - Siga as instruções na tela para inserir valores e confirmar operações.

## Estrutura do Código

- **Variáveis Globais:** `saldo` e `extrato` para armazenar o saldo atual e o histórico de transações.
- **Funções:**
  - `formatar_moeda(valor)`: Formata valores monetários no padrão brasileiro.
  - `operacao_deposito(valor)`: Realiza a operação de depósito.
  - `operacao_saque(valor)`: Realiza a operação de saque.
  - `operacao_extrato()`: Exibe o extrato das transações e o saldo atual.

## Exemplo de Uso

1. Escolha a opção de depósito no menu.
2. Insira o valor do depósito.
3. Confirme se deseja fazer outro depósito ou voltar ao menu principal.
4. Escolha a opção de extrato para visualizar as transações e o saldo atual.

## Contribuição

Este projeto foi desenvolvido como parte de um exercício acadêmico. Contribuições e sugestões são bem-vindas para melhorar e expandir as funcionalidades do sistema.
