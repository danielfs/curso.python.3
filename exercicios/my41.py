class Cancao(object):

	def __init__(self, titulo, letra):
		self.titulo = titulo
		self.letra = letra
	
	def cante_me_uma_cancao(self):
		self.mostrar_titulo()
		
		for linha in self.letra:
			print(linha)
	
	def mostrar_titulo(self):
		print('-' * 40)
		print(self.titulo)
		print('-' * 40)

feliz_aniversario = Cancao(
	'Parabéns pra você',
	[
		'Parabéns pra você',
		'Nesta data querida',
		'Muitas felicidades',
		'Muitos anos de vida'
	]
)

nao_atire_o_pau_no_gato = Cancao(
	'Não atire o pau no gato',
	[
		'Não atire o pau no gato-to',
		'Porque isto-to',
		'Não se faz-faz-faz',
		'O gatinho-nho',
		'É nosso amigo-go',
		'Não devemos maltratar os animais',
		'Jamais!'
	]
)

feliz_aniversario.cante_me_uma_cancao()
nao_atire_o_pau_no_gato.cante_me_uma_cancao()
