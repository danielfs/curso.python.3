i = 0
numeros = []

while i < 6:
	print("Aqui em cima o i vale %d" % i)
	numeros.append(i)
	
	i = i + 1
	print("A lista número agora é:", numeros)
	
	print("Aqui embaixo o i vale %d" % i)

print("Todos os números adicionados:")

for n in numeros:
	print(n)
