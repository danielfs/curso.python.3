from sys import argv

script, nome_arquivo = argv

print("Nós apagaremos o arquivo %r." % nome_arquivo)
print("Se você não quiser, aperte CTRL-C (^C).")
print("Se você não se importa, aperte ENTER.")

input("?")

print("Abrindo o arquivo...")
arquivo = open(nome_arquivo, "w")

print("Apagando o arquivo. Tchau!")
arquivo.truncate()

print("Agora eu vou te pedir que digite 3 linhas.")

linha1 = input("1: ")
linha2 = input("2: ")
linha3 = input("3: ")

print("Escrevendo as linhas no arquivo.")

arquivo.write(linha1)
arquivo.write("\n")
arquivo.write(linha2)
arquivo.write("\n")
arquivo.write(linha3)
arquivo.write("\n")

print("E finalmente, fechando o arquivo.")
arquivo.close()
