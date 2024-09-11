def analise_vendas(vendas):
    total_vendas = 0

    # Calculando o total de vendas
    for venda in vendas:
        total_vendas += venda

    # Calculando a média mensal
    media_vendas = total_vendas/12

    return f"{total_vendas}, {media_vendas:.2f}"


def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada_str = input()

    vendas = list(map(int, entrada_str.split(", ")))

    return vendas


vendas = obter_entrada_vendas()
# print(vendas)
print(analise_vendas(vendas))
