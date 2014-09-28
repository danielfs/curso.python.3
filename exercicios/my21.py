from sys import argv

script, arquivo_entrada = argv

def mostrar_tudo(arquivo):
	print(arquivo.read())

def voltar_ao_inicio(arquivo):
	arquivo.seek(0)

def imprimir_uma_linha(contador, arquivo):
	print(contador, arquivo.readline())

arquivo_atual = open(arquivo_entrada)

print("Primeiro vamos imprimir o arquivo completo:\n")
mostrar_tudo(arquivo_atual)

print("Agora vamos voltar ao início do arquivo.")
voltar_ao_inicio(arquivo_atual)

print("Vamos imprimir 3 linhas:")

linha_atual = 1
imprimir_uma_linha(linha_atual, arquivo_atual)

linha_atual = linha_atual + 1
imprimir_uma_linha(linha_atual, arquivo_atual)

linha_atual += 1
imprimir_uma_linha(linha_atual, arquivo_atual)
