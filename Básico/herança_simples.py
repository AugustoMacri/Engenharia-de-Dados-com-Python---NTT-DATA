class Veiculo:
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas

    def ligar_motor(self):
        print("ligar motor")


class Carro(Veiculo):
    pass


class Moto(Veiculo):
    def empinar(self):
        print("Empinando")


class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carregado):
        super().__init__(cor, placa, rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'sim' if self.carregado else 'nao'}")



moto = Moto("azul", "abc1234", 2)
moto.ligar_motor()
moto.empinar()

carro = Carro("preto", "acd134", 4)
carro.ligar_motor()

caminhao = Caminhao("vermelho", "agh567", 8, '')
caminhao.esta_carregado()