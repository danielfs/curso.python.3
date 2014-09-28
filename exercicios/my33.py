numeros = [1, 2, 3, 4, 5]
frutas = ['maçã', 'laranja', 'mamão', 'limão']
diversos_tipos = [1, 'caderno', 2, 'carro', 'nave espacial']

for numero in numeros:
	print("Número: %d" % numero)

for i in diversos_tipos:
	print("Há um elemento com o valor %r." % i)

for fruta in frutas:
	print("Eu gosto de: %s" % fruta)

elementos = []

for i in range(0, 6):
	print("Adicionando %d à lista." % i)
	elementos.append(i)

for i in elementos:
	print("O elemento encontrado foi: %d" % i)
