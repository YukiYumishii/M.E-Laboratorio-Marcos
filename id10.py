numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def pulverizar_duplicatas(numeros):
    lista_nova = []
    for numero in numeros:
        if numero not in lista_nova:
            lista_nova.append(numero)
    return lista_nova

print(pulverizar_duplicatas(numeros))