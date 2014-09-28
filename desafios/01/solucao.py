class MaiorMenor(object):
	def __init__(self):
		self.maior = 0
		self.menor = 100

quantidade_alunos_por_turma = {
	1: 0,
	2: 0,
	3: 0,
	4: 0,
	5: 0
}

pontos_por_turma = {
	1: 0,
	2: 0,
	3: 0,
	4: 0,
	5: 0
}

maior_e_menor_por_turma = {
	1: MaiorMenor(),
	2: MaiorMenor(),
	3: MaiorMenor(),
	4: MaiorMenor(),
	5: MaiorMenor()
}

def conta_aluno_turma(turma):
	quantidade_alunos_por_turma[ turma ] += 1

def media_aluno(*notas):
	soma = 0
	quantidade = 0
	
	for nota in notas:
		soma += nota
		quantidade += 1
	
	media = soma / quantidade
	
	return media

def adiciona_pontos_para_turma(turma, pontos):
	pontos_por_turma[turma] += pontos

def recalcula_maior_e_menor_nota_da_turma(turma, nota):
	objeto = maior_e_menor_por_turma[turma]
	
	if nota > objeto.maior:
		objeto.maior = nota
		
	if nota < objeto.menor:
		objeto.menor = nota

def calcular():
	dados = open('dados.in')
	
	for linha in dados:
		nome, turma, nota1, nota2, nota3, nota4, nota5 = linha.split(';')
		
		# converte para inteiro
		turma = int(turma)
		nota1 = int(nota1)
		nota2 = int(nota2)
		nota3 = int(nota3)
		nota4 = int(nota4)
		nota5 = int(nota5)
		
		# adiciona mais um aluno na turma
		conta_aluno_turma(turma)
		
		# calcula média do aluno
		media = media_aluno(nota1, nota2, nota3, nota4, nota5)
		
		# acrescenta nota do aluno na turma
		adiciona_pontos_para_turma(turma, media)
		
		# recalcula maior e menor nota por turma
		recalcula_maior_e_menor_nota_da_turma(turma, media)

def mostrar_titulo(titulo):
	espacos = int((80 - len(titulo)) / 2)
	print()
	print('%s %s %s' % ('*' * espacos, titulo, '*' * espacos))

def mostrar_quantidade_de_alunos_por_turma():
	mostrar_titulo('Quantidade de Alunos Por Turma')
	for i in quantidade_alunos_por_turma:
		quantidade = quantidade_alunos_por_turma[i]
		print('Turma %d: %d alunos.' % (i, quantidade))
	
	print()

def mostrar_media_de_pontos_por_turma():
	mostrar_titulo('Média de Pontos por Turma')
	
	for turma in range(1, 6):
		alunos = quantidade_alunos_por_turma[turma]
		pontos = pontos_por_turma[turma]
		
		media = pontos / alunos
		
		print('Turma %d: %.2f pontos.' % (turma, media))
	
	print()

def mostrar_maior_e_menor_nota_por_turma():
	mostrar_titulo('Maior e Menor Nota por Turma')
	
	for i in maior_e_menor_por_turma:
		objeto = maior_e_menor_por_turma[i]
		
		maior = objeto.maior
		menor = objeto.menor
		
		print('Turma %d: %.2f (maior), %.2f (menor)' % (i, maior, menor))
	
	print()

def mostrar_media_de_pontos_da_escola():
	mostrar_titulo('Média de Pontos da Escola')
	
	soma = 0
	
	for i in maior_e_menor_por_turma:
		objeto = maior_e_menor_por_turma[i]
		
		maior = objeto.maior
		menor = objeto.menor
		
		media = (maior + menor) / 2
		
		soma += media
	
	media = soma / 5
	
	print('Média: %.2f' % media)
	print()

def mostrar_maior_e_menor_nota_da_escola():
	mostrar_titulo('Maior e Menor Nota da Escola')
	
	maior = 0
	menor = 100
	
	for i in maior_e_menor_por_turma:
		objeto = maior_e_menor_por_turma[i]
		
		if objeto.maior > maior:
			maior = objeto.maior
		if objeto.menor < menor:
			menor = objeto.menor
	
	print('Notas: %.2f (maior), %.2f (menor)' % (maior, menor))
	print()

def mostrar_informacoes():
	mostrar_quantidade_de_alunos_por_turma()
	mostrar_media_de_pontos_por_turma()
	mostrar_maior_e_menor_nota_por_turma()
	mostrar_media_de_pontos_da_escola()
	mostrar_maior_e_menor_nota_da_escola()

def resolver_problema():
	calcular()
	mostrar_informacoes()

resolver_problema()
