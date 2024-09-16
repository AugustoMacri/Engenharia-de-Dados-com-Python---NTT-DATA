def exibit_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

    #kwargs é uma estrutura chave e valor, então o python sabe quando o poema vai parar quando estiver
    #com chave e valor 

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

    #Os que vem depois da barra, podem ser nomeados ou apenas por posição

exibit_poema(
    "Sexta-feira",
    "Zen of python", 
    "Beutiful is better than ugly.",
    autor="Tim Peters", 
    ano=1999
)

criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")