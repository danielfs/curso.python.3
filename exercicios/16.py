from sys import argv

script, nome_arquivo = argv

txt = open(nome_arquivo)

print("Este é o seu arquivo %r: " % nome_arquivo)
print(txt.read())

arquivo_novamente = input("Digite o nome do arquivo novamente: ")
txt_novamente = open(arquivo_novamente)

print(txt_novamente.read())
