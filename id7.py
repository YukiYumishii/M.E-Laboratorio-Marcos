cafes = [
    {'nome': 'Espresso'},
    {'nome': 'Americano'},
    {'nome': 'Latte'},
    {'nome': 'Cappuccino'},
    {'nome': 'Descafeinado'},
]


def extrair_nome(cafes):
    nomes = []
    for cafe in cafes:
        nomes.append(cafe['nome'])
    return nomes

print(extrair_nome(cafes))


