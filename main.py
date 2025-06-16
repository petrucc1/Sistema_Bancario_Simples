# Inicializa o saldo e a lista de extrato
saldo = 0
extrato = []

def formatar_moeda(valor):
    # Formata o valor como moeda brasileira
    return f"R${valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

# Função para realizar um depósito
def operacao_deposito(valor):
    global saldo
    if valor <= 0:
        print('Ops! É necessário inserir um valor válido para depósito.')
    else:
        saldo += valor
        # Adiciona a transação ao extrato formatando o valor como moeda
        extrato.append(f'Depósito: {formatar_moeda(valor)}')
        print('Depósito realizado com sucesso!')

# Função para realizar um saque
def operacao_saque(valor):
    global saldo
    if valor <= 0:
        print('Você precisa inserir um valor válido para saque.')
    elif valor > saldo:
        print('Você não possui saldo suficiente.')
    elif valor > 500:
        print('O limite por saque é de R$500,00. Por favor, insira um novo valor dentro do limite.')
    else:
        saldo -= valor
        # Adiciona a transação ao extrato formatando o valor como moeda
        extrato.append(f'Saque: {formatar_moeda(valor)}')
        print('Saque realizado com sucesso!')

# Função para exibir o extrato
def operacao_extrato():
    print('\nExtrato:')
    for transacao in extrato:
        print(transacao)
    # Exibe o saldo atual formatado como moeda
    print(f'Saldo atual: {formatar_moeda(saldo)}')
    print()

# Loop principal do programa
while True:
    try:
        # Exibe o menu de opções
        print("\nEscolha uma das opções:")
        print("[1]: Depósito")
        print("[2]: Saque")
        print("[3]: Extrato")
        print("[4]: Sair")

        # Captura a opção escolhida pelo usuário
        option = int(input("Opção: "))

        if option == 1:
            # Loop para realizar múltiplos depósitos
            while True:
                valor = float(input("\nDigite o valor do depósito: "))
                operacao_deposito(valor)
                # Loop para validar a entrada do usuário
                while True:
                    voltar = input("\nDeseja fazer outro depósito? (s/n): ").strip().lower()
                    if voltar in ('s', 'n'):
                        break
                    print("Entrada inválida. Por favor, digite 's' ou 'n'.")
                if voltar != 's':
                    break
        elif option == 2:
            # Loop para realizar múltiplos saques
            while True:
                valor = float(input("\nDigite o valor do saque: "))
                operacao_saque(valor)
                # Loop para validar a entrada do usuário
                while True:
                    voltar = input("\nDeseja fazer outro saque? (s/n): ").strip().lower()
                    if voltar in ('s', 'n'):
                        break
                    print("Entrada inválida. Por favor, digite 's' ou 'n'.")
                if voltar != 's':
                    break
        elif option == 3:
            # Exibe o extrato
            operacao_extrato()
            input("Pressione Enter para voltar ao menu principal.")
        elif option == 4:
            # Sai do loop principal e encerra o programa
            break
        else:
            print("Insira um número válido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
