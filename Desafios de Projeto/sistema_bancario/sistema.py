# Desafio - Criar um ssitema bancário com, sacar, deposito e visualizar extrato

def deposito(valor, saldo):
    saldo += valor

    extrato.append(f"Deposito: + R${valor}")

    return saldo


def saque(valor_saque, num_saques, saldo, saques_diarios):

    if num_saques < saques_diarios and valor_saque <= 500 and valor_saque < saldo:

        saldo -= valor_saque
        extrato.append(f"Deposito: - R${valor_saque}")
        num_saques = num_saques + 1

    elif (valor_saque > saldo):
        print("Saldo insuficiente")

    else:
        print("Número de saques diarios atingido ou valor excedeu 500")

    return saldo, num_saques


def extrato_bancario(extrato, saldo):
    print("---------------------------")
    print("|         Extrato         |")
    print("---------------------------")

    if extrato:

        for transacao in extrato:
            print(transacao)

    else:
        print("Nenhuma transação foi realizada")

    print(f"Saldo Autal: {saldo}")
    print("---------------------------")


saldo = 0
num_saques = 0
saques_diarios = 3
extrato = []

while True:

    print("---------------------------")
    print("|        Bem-Vindo        |")
    print("---------------------------")
    print("|    Escolha uma opção    |")
    print("|1 - Realizar depósito    |")
    print("|2 - Realizar Saque       |")
    print("|3 - Visualizar extrato   |")
    print("|4 - Sair                 |")
    print("---------------------------")

    opcao = int(input())

    if opcao == 1:
        valor_deposito = int(
            input("Digite o valor que gostaria de depositar:"))

        saldo = (deposito(valor_deposito, saldo))

    elif opcao == 2:
        valor_saque = int(input("Digite o valor que gostaria de sacar:"))

        saldo, num_saques = (
            saque(valor_saque, num_saques, saldo, saques_diarios))

    elif opcao == 3:
        extrato_bancario(extrato, saldo)

    elif opcao == 4:
        print("Até a próxima")

        break
