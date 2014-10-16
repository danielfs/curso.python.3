from curso.conexao import get_pagina_globoesporte
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.pode_imprimir = 0
		
	def handle_starttag(self, tag, attrs):
		if self.tag_classificacao(tag, attrs):
			self.pode_imprimir = 'classificacao'
		elif self.tag_nome_time(tag, attrs):
			self.pode_imprimir = 'nome-time'
		elif self.tag_pontos_ganhos(tag, attrs):
			self.pode_imprimir = 'total-pontos'
	
	def handle_data(self, data):
		if self.pode_imprimir == 'classificacao':
			print('{:<13d}'.format(int(data)), end='   ')
		elif self.pode_imprimir == 'nome-time':
			print('{:<13s}'.format(data), end='   ')
		elif self.pode_imprimir == 'total-pontos':
			print('{:<13d}'.format(int(data)))
		
		self.pode_imprimir = 0
	
	def tag_classificacao(self, tag, attrs):
		if tag == 'td' and ('rel', 'grafico-posicao') in attrs:
			return True
		
		return False
	
	def tag_nome_time(self, tag, attrs):
		if tag == 'strong' and ('itemprop', 'name') in attrs:
			return True
		
		return False
	
	def tag_pontos_ganhos(self, tag, attrs):
		if tag == 'td' and ('rel', 'jogos-pontos') in attrs:
			return True
		
		return False

def iniciar():
	conteudo = get_pagina_globoesporte()
	parser = MyHTMLParser()
	
	print('{:<13s}   {:<13s}   {:<13s}'.format('Classificação', 'Time', 'Pontos Ganhos'))
	parser.feed(conteudo)

iniciar()
