dez_coisas = "Maças Laranjas Bicicletas Telefones Luz Açúcar"

print(dez_coisas)
print("Espere! Não há 10 coisas na list. Vamos corrigi-la.")

coisas = dez_coisas.split(' ')
mais_coisas = ["Dia", "Noite", "Música", "Python", "Guitarra", "Banana"]

while len(coisas) != 10:
	proximo = mais_coisas.pop()

	print("Adicionando:", proximo)
	
	coisas.append(proximo)
	
	print("Agora há %d coisas na lista." % len(coisas))

print("Aqui estão:", coisas)
print("Vamos fazer algumas operações com a lista:")

print(coisas[1])
print(coisas[-2])
print(coisas.pop())
print(' '.join(coisas))
print('#'.join(coisas[3:5]))
