class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo


class Oviparo(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Oviparo):
    pass


gato = Gato(nro_patas=4, cor_pelo="preto")
print(gato.nro_patas)

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="preto", cor_bico="amarelo")
print(ornitorrinco)
