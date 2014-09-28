def queijo_e_bolachas(qtde_queijo, qtde_caixa_bolacha):
	print("Você tem %d queijos!" % qtde_queijo)
	print("Você tem %d caixas de bolacha!" % qtde_caixa_bolacha)
	print("Cara, isto é o suficiente para um café da manhã.")
	print("Pegue um cobertor.\n")

print("Podemos invocar as funções informando os valores diretamente:")
queijo_e_bolachas(20, 30)

print("Ou podemos usar variáveis no nosso código:")
quantidade_queijo = 10
quantidade_caixa_bolacha = 50

queijo_e_bolachas(quantidade_queijo, quantidade_caixa_bolacha)

print("Podemos inclusive utilizar operações matemáticas:")

queijo_e_bolachas(10 + 20, 5 + 6)

print("E ainda podemos combinar variáveis e matemática:")
queijo_e_bolachas(quantidade_queijo + 100, quantidade_caixa_bolacha + 1000)
