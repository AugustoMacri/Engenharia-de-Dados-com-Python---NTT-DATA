class Passaro:
    def voar(self):
        print("voar..")

class Pardal(Passaro):
    def voar(self):
        return super().voar()


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_de_voo(obj):
    obj.voar()

avestruz = Avestruz()
plano_de_voo(avestruz)