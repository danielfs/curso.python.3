# Problema B: esquerda

direcao = 'N'

def girar_esquerda():
	global direcao
	
	if direcao == 'N':
		direcao = 'O'
	elif direcao == 'O':
		direcao = 'S'
	elif direcao == 'S':
		direcao = 'L'
	elif direcao == 'L':
		direcao = 'N'

def girar_direita():
	global direcao
	
	if direcao == 'N':
		direcao = 'L'
	elif direcao == 'L':
		direcao = 'S'
	elif direcao == 'S':
		direcao = 'O'
	elif direcao == 'O':
		direcao = 'N'

def calcular_direcao(comando):
	if comando == 'E':
		girar_esquerda()
	elif comando == 'D':
		girar_direita()

def imprimir_direcao():
	global direcao
	
	print(direcao)

def iniciar():

	n = int(input())
	comandos = input()

	for i in range(0, n):
		comando = comandos[ i ]

		calcular_direcao(comando)

	imprimir_direcao()

iniciar()
