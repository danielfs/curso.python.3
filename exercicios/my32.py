print("Ano 4102. Você entrou em uma sala escura com duas portas. Você vai pela porta #1 ou pela porta #2?")

porta = input("> ")

if porta == "1":
	print("Há um urso gigante comendo um bolo de cenoura. O que você faz?")
	print("1. Pega o bolo.")
	print("2. Grita com o urso.")
	
	urso = input("> ")
	
	if urso == "1":
		print("Bom trabalho! O urso comeu sua cabeça.")
	elif urso == "2":
		print("Bom trabalho! O urso comeu suas pernas.")
	else:
		print("Bem, fazendo %s é provavelmente melhor. O grande urso foi embora." % urso)
elif porta == "2":
	print("Você fez uma viagem no tempo para o ano de 2014 e veio parar nesta sala com um curso sobre Python! O que você faria?")
	
	print("1. Programaria em Python na versão 1.577.341.980")
	print("2. Tentaria aprender a versão 3.4 de 2014")
	print("3. Eu não sou programador")
	
	escolha = input("> ")
	
	if escolha == "1" or escolha == "2":
		print("Junte-se à turma, pythoniano.")
	else:
		print("Esta piada foi boa! Conte-me mais uma.")
else:
	print("Você caiu dentro de um recipiente gigante, cheio de gelatina.")
