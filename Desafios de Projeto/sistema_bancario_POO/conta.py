from historico import Historico


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_Conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        excedeu = self.saldo + valor

        if excedeu:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            return True

        return False

    def depositar(self, valor):
        if (valor > 0):
            self.saldo += valor
            return True
        else:
            return False    