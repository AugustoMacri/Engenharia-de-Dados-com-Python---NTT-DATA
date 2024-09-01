# Desafio2 - Criar um sitema bancário com, sacar, deposito e visualizar extrato
# - Estabelecendo um limite de 10 trnsações diárias para uma conta
# - Se o usuário tentar realizar uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas no dia
# - Mostre a data e hora das transações no extrato

import datetime as dt

# Lista para armazenar transacoes
transacoes = []


def deposito(valor, saldo, num_transacao_hoje, transacoes_diarias):
    data = dt.datetime.now()

    if num_transacao_hoje >= transacoes_diarias:
        print("Limite atingido")
        return saldo

    saldo += valor
    transacoes.append({'tipo': 'deposito', 'valor': valor, 'data': data})
    extrato.append(f"Deposito: + R${valor} {data}")

    return saldo


def saque(valor_saque, num_saques, saldo, num_transacoes_hoje, transacoes_diarias):

    data = dt.datetime.now()

    if num_transacoes_hoje < transacoes_diarias and valor_saque < saldo:

        saldo -= valor_saque

        transacoes.append(
            {'tipo': 'deposito', 'valor': valor_saque, 'data': data})
        extrato.append(f"Deposito: - R${valor_saque} {data}")
        num_saques = num_saques + 1

    elif (valor_saque > saldo):
        print("Saldo insuficiente")

    else:
        print("Número de saques diarios atingido")

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
transacoes_diarias = 10
extrato = []

# Extraindo o dia de hoje
data = dt.datetime.now()
data_hoje = data.day


while True:

    num_transacao_hoje = sum(1 for transacao in transacoes if (
        transacao['tipo'] == 'deposito' or transacao['tipo'] == 'saque') and transacao['data'].date() == data.date())

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

        saldo = (deposito(valor_deposito, saldo,
                 num_transacao_hoje, transacoes_diarias))

    elif opcao == 2:
        valor_saque = int(input("Digite o valor que gostaria de sacar:"))

        saldo, num_saques = (
            saque(valor_saque, num_saques, saldo, num_transacao_hoje, transacoes_diarias))

    elif opcao == 3:
        extrato_bancario(extrato, saldo)

    elif opcao == 4:
        print("Até a próxima")

        break
