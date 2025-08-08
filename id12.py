natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

def juntar_listas(lista1, lista2):
    lista_junta = []
    for item in lista1:
        if item not in lista_junta:
            lista_junta.append(item)
    for item in lista2:
        if item not in lista_junta:
            lista_junta.append(item)
    return lista_junta

print(juntar_listas(natureza, tecnologia))