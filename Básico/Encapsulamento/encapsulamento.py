class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo  # definida como privado

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta(100)
# print(conta._saldo) #VAI FUNCIONAR MAS NAO DEVE OCORRER

# Para depositar por exemplo
conta.depositar(100)

# Para acessar o valor de uma variavel privada, o certo eh criar um metodo
print(conta.mostrar_saldo())
