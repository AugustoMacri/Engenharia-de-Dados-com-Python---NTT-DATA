# Desafio2 - Criar um sitema bancário com, sacar, deposito e visualizar extrato
# - Estabelecendo um limite de 10 trnsações diárias para uma conta
# - Se o usuário tentar realizar uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas no dia
# - Mostre a data e hora das transações no extrato
# - Tornar possível cadastrar um usuario
# - Vincular esse cliente a uma conta

import datetime as dt
from cliente import Cliente

# Lista para armazenar transacoes
transacoes = []

# Lista para armazenar os clientes
lista_clientes = []

# Dicionario para clientes com conta
lista_clientes_conta = {}

numero_conta = 0000


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


def cadastrarUsuario():
    print("Digite as seguintes credenciais:")
    nome = input("nome: ")
    sexo = input("sexo: ")
    cpf = input("cpf: ")
    endereco = input("Endereco: ")

    # Criando o objeto cliente
    cliente = Cliente(nome, sexo, cpf, endereco)

    lista_clientes.append(cliente)

    return cliente


def criarContaCorrente():
    global numero_conta

    print("Deseja criar uma conta para qual cpf?")
    cpf = input()

    for cliente in lista_clientes:
        if cliente.cpf == cpf:
            print("Cliente encontrado")
            dict1 = {cliente.cpf: numero_conta}

            lista_clientes_conta.update(dict1)

            numero_conta += 1

            return 1

    print("Cliente nao encontrado")
    return 0


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
    print("|1 - Cadastrar Cliente    |")
    print("|2 - Criar Conta          |")
    print("|3 - Realizar depósito    |")
    print("|4 - Realizar Saque       |")
    print("|5 - Visualizar extrato   |")
    print("|6 - Sair                 |")
    print("---------------------------")

    opcao = int(input())

    if opcao == 1:
        cadastrarUsuario()

    elif opcao == 2:
        criarContaCorrente()

    elif opcao == 3:
        valor_deposito = int(
            input("Digite o valor que gostaria de depositar:"))

        saldo = (deposito(valor_deposito, saldo,
                 num_transacao_hoje, transacoes_diarias))

    elif opcao == 4:
        valor_saque = int(input("Digite o valor que gostaria de sacar:"))

        saldo, num_saques = (
            saque(valor_saque, num_saques, saldo, num_transacao_hoje, transacoes_diarias))

    elif opcao == 5:
        extrato_bancario(extrato, saldo)

    elif opcao == 6:
        print("Até a próxima")

        break
