class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod #ira transformar em um metodo de classe
    def criar_apartir_datanasc(cls, ano, mes, dia, nome): #nao utiliza self, mas sim, cls
        idade = 2024 - ano
        return cls(nome, idade)

    #metodo estatico
    @staticmethod
    def eh_maior_idade(idade):
        return idade >= 18

p = Pessoa("augusto", 20)

p2 = Pessoa.criar_apartir_datanasc(2003, 10, 17, "Augusto")
print(p2.nome, p2.idade)

print(Pessoa.eh_maior_idade(20))
