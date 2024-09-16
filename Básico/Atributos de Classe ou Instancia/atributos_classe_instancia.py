class Estudante:
    escola = "DIO" #Variavel de classe

    def __init__(self, nome, matricula):
        self.nome = nome #Variavel de instancia
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


estudante = Estudante("Augusto", 1)
estudante2 = Estudante("Sarah", 2)

Estudante.escola = "UFU" #Variavel de classe
print(estudante)
print(estudante2)