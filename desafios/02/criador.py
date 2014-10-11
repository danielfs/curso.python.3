import random

def caractere_aleatorio():
	escolha = random.choice(['letra_maiuscula', 'letra_minuscula', 'numero'])
	
	if escolha == 'letra_maiuscula':
		caractere = random.randint(65, 90)
		return str(chr(caractere))
	elif escolha == 'letra_minuscula':
		caractere = random.randint(97, 122)
		return str(chr(caractere))
	elif escolha == 'numero':
		return str(random.randint(0, 9))

def criar():
	arquivo = open('dados.in', 'w')
	
	MAX = 200
	
	linhas = MAX
	colunas = MAX
	
	while linhas >= 1:
		linha = ''
		while colunas >= 1:
			caractere = caractere_aleatorio()
			linha = linha + caractere
			
			colunas = colunas - 1
			
		arquivo.write(linha + '\n')
		linhas -= 1
		colunas = MAX
	
	arquivo.close()
			

criar()
