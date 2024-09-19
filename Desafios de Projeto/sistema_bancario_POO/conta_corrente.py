from conta import Conta
from transacao_interface import Transacao

class Conta_corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)  
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque

        if excedeu_limite:
            print("excedeu o limite")
        elif excedeu_saques:
            print("excedeu saque")
        else:
            return super().sacar(valor)
        
        return False
   
