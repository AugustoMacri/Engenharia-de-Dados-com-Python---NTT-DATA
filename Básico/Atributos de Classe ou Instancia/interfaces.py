from abc import ABC, abstractclassmethod


class controleRemoto(ABC):  # Nao pode mais ser instanciada

    @abstractclassmethod
    def ligar():
        pass

    @abstractclassmethod
    def desligar():
        pass


class controleTV(controleRemoto):
    def ligar(self):
        pass

    def desligar(self):
        pass


controle = controleTV()
