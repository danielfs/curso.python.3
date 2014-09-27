# criando um dicionário de estados para abreviação
estados = {
	'Minas Gerais': 'MG',
	'São Paulo': 'SP',
	'Rio de Janeiro': 'RJ',
	'Acre': 'AC',
	'Bahia': 'BA',
	'Amazonas': 'AM'
}

# dicionário de cidades
cidades = {
	'MG': 'Belo Horizonte',
	'SP': 'São Paulo',
	'RJ': 'Rio de Janeiro',
	'AC': 'Rio Branco'
}

# adicionando mais algumas cidades
cidades['BA'] = 'Salvador'
cidades['AM'] = 'Manaus'

# mostrando algumas cidades
print('-' * 10)
print('O estado AM tem:', cidades['AM'])
print('O estado MG tem:', cidades['MG'])

# alguns estados
print('-' * 10)
print('A abreviação do estado Acre é:', estados['Minas Gerais'])
print('A abreviação do estado São Paulo é:', estados['São Paulo'])

# usando os dois dicionários ao mesmo tempo
print('-' * 10)
print('O estado Rio de Janeiro tem:', cidades[estados['Rio de Janeiro']])
print('O estado Bahia tem:', cidades[estados['Bahia']])

# mostrar todas as abreviações dos estados
print('-' * 10)
for estado, abreviacao in estados.items():
	print('A abreviação de %s é %s' % (estado, abreviacao))

# mostrar as cidades dos estados
print('-' * 10)
for abreviacao, cidade in cidades.items():
	print('A cidade %s está no estado %s' % (cidade, abreviacao))

# agora tudo junto
print('-' * 10)
for estado, abreviacao in estados.items():
	print('A abreviação do estado %s é %s e ele possui a cidade %s' % (estado, abreviacao, cidades[abreviacao]))

print('-' * 10)

# obtendo um estado que não está no dicionário
estado = estados.get('Rio Grande do Sul', None)

if not estado:
	print('Infelizmente não foi localizado o estado Rio Grande do Sul.')

# obtendo um cidade com um valor padrão
cidade = cidades.get('PA', 'Cidade não existe')

print("A cidade para o estado 'PA' é: %s" % cidade)
