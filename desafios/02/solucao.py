import re

def resolver():
	arquivo = open('dados.in', 'r')
	palavras = ['PYTHON', 'CADA', 'VEZ', 'MAIS', 'COBRA']
	
	i = 1
	soma = 0
	
	for linha in arquivo:
		for palavra in palavras:
			resultado = re.search(palavra, linha)
			if resultado != None:
				print('Palavra %s encontrada na linha %d' % (palavra, i))
				soma = soma + i
		
		i = i + 1
	
	print('A soma é %d' % soma)

resolver()
