# esta funciona da mesma maneira que os argumentos pela linha de comando
def mostra_dois_argumentos(*args):
	arg1, arg2 = args
	print("arg1: %r, arg2: %r" % (arg1, arg2))

# esta é uma outra forma de receber mais de um argumento
def mostra_dois_argumentos_novamente(arg1, arg2):
	print("arg1: %r, arg2: %r" % (arg1, arg2))

# esta recebe apenas um argumento
def mostra_um(arg1):
	print("arg1: %r" % arg1)

# esta recebe nenhum argumento
def mostra_nada():
	print(":( Não recebi nenhum argumento.")

mostra_dois_argumentos("Curso", "Python")
mostra_dois_argumentos_novamente("Curso", "Python")
mostra_um("Curso")
mostra_nada()
