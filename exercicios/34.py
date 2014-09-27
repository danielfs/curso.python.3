contador = 0
numeros = []

while contador < 6:
    print("Adicionando %d" % contador)
    numeros.append(contador)
    contador = contador + 1  # ou contador += 1
    print("Númeos até agora", numeros)

print("Imprimindo os números")
for numero in numeros:
    print(numero)
