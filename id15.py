numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def inverter(lista):
    lista_invertida = []
    for item in lista:
        lista_invertida.insert(0, item)
    return lista_invertida

print(inverter(numeros))