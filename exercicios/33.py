contador = [1, 2, 3, 4, 5]
frutas = ['maçãs', 'laranjas', 'pêras', 'damascos']
mudar = [1, 'centavos', 2, '10 centavos', 3, 'trimestres']

for numero in contador:
    print("O contador tem esse número: %s" % numero)

for fruta in frutas:
    print("A fruta é do tipo: %s" % fruta)

# nós podemos andar em listas mistas, ou seja, com elementos de vários
# tipos

for i in mudar:
    print("Eu tenho %r" % i)

# nós podemos criar listas vazias
elementos = []

# e usar a função rnage para preenche-lá

for numero in range(0, 6):
    print("Adicionando %d na lista" % numero)
    elementos.append(numero)

# agora podemos imprimir a lista que criamos
for elemento in elementos:
    print("Elemento: %d" % elemento)
