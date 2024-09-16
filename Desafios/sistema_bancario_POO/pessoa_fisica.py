from cliente import Cliente

class Pessoa_Fisica(Cliente):
    def __init__(self, endereco, nome, data_nasc, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.adata_nasc = data_nasc
        self.cpf = cpf