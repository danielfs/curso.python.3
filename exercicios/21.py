from sys import argv


def imprimir_tudo(arquivo_entrada):
    with open(arquivo_entrada) as arquivo:
        print(arquivo.read())


def imprimir_uma_linha(linha, arquivo_entrada):
    with open(arquivo_entrada) as arquivo:
        print(linha, arquivo.readline())


def rebobinar(arquivo_entrada):
    with open(arquivo_entrada) as arquivo:
        arquivo.seek(0)


script, arquivo_entrada = argv

print("Vamos primeiramente imprimir todo o arquivo:\n")
imprimir_tudo(arquivo_entrada)

print("Agora vamos rebobinar, como um tipo de fita.")
rebobinar(arquivo_entrada)

print("Vamos imprimir 3 linhas, uma de cada vez:")

linha_atual = 1
imprimir_uma_linha(linha_atual, arquivo_entrada)

linha_atual = linha_atual + 1
imprimir_uma_linha(linha_atual, arquivo_entrada)

linha_atual = linha_atual + 1
imprimir_uma_linha(linha_atual, arquivo_entrada)
