import random

contador_turma = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 }


# sorteia o número da turma
def turma_aleatoria():
	numero_turma = random.randint(1, 5)
	
	while contador_turma[ numero_turma ] >= 40:
		numero_turma = random.randint(1, 5)
	
	contador_turma[ numero_turma ] += 1
	
	return numero_turma


# sorteia nota
def nota_aleatoria():
	nota = random.randint(50, 100)
	return nota


# cria o arquivo aleatoriamente
def criar():
	print('Criando arquivo...')
	
	arquivo = open('dados.in', 'w')
	
	nomes = open('nomes.in')
	
	for nome in nomes:
		turma = turma_aleatoria()
		nota1 = nota_aleatoria()
		nota2 = nota_aleatoria()
		nota3 = nota_aleatoria()
		nota4 = nota_aleatoria()
		nota5 = nota_aleatoria()
		
		arquivo.write('%s;%d;%d;%d;%d;%d;%d\n' % (nome[:-1], turma, nota1, nota2, nota3, nota4, nota5))
	
	arquivo.close()
	print('Arquivo criado com sucesso!')

criar()
