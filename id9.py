numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def contar_ocorrencias(valor, numeros):
    contador = 0
    for numero in numeros:
        if numero == valor:
            contador += 1
    return contador

print(contar_ocorrencias(9, numeros))
