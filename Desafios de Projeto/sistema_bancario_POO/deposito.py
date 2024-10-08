from transacao_interface import Transacao
from conta import Conta

class Deposito(Transacao):
    def __init__(self, valor):
        super()._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)