def soma(a, b):
	print("Somando %d + %d" % (a, b))
	return a + b

def subtracao(a, b):
	print("Subtraindo %d - %d" % (a, b))
	return a - b

def multiplicacao(a, b):
	print("Multiplicando %d * %d" % (a, b))
	return a * b

def divisao(a, b):
	print("Dividindo %d / %d" % (a, b))
	return a / b

print("Vamos fazer algumas operações com estas funções!")

idade = soma(10, 13)
altura = subtracao(100, 16)
peso = multiplicacao(42, 2)
qi = divisao(150, 2)

print("Idade: %d, Altura: %d, Peso: %d, QI: %d" % (idade, altura, peso, qi))

print("Quebra-Cabeça:")

misterio = soma(idade, subtracao(altura, multiplicacao(peso, divisao(qi, 2))))

print("Qual é o resultado?", misterio)
