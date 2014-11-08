import gspread
gc = gspread.login('<seu-email>@gmail.com', '<sua-senha>')
sh = gc.open('Dados da Escola')
planilha = sh.add_worksheet(title="Daniel", rows="201", cols="7")

def ler_arquivo():
	arquivo = open('dados.in')
	return arquivo

def criar_cabecalho():
	numero_linha = 1
	valores = [
		'Nome do Aluno',
		'Turma',
		'Nota 1',
		'Nota 2',
		'Nota 3',
		'Nota 4',
		'Nota 5'
	]
	
	criar_linha(numero_linha, valores)

def criar_linha(numero_linha, valores):
	intervalo = 'A' + str(numero_linha) + ':G' + str(numero_linha)
	celulas = planilha.range(intervalo)
	
	for celula, valor in zip(celulas, valores):
		celula.value = valor
	
	planilha.update_cells(celulas)

def tratar_linha(numero_linha, linha):
	valores = linha.split(';')
	
	criar_linha(numero_linha, valores)

def iniciar():
	arquivo = ler_arquivo()
	
	criar_cabecalho()
	
	i = 2
	
	for linha in arquivo:
		tratar_linha(i, linha)
		i = i + 1
	
	arquivo.close()

iniciar()
