from sys import argv
from os.path import exists

script, arquivo_origem, arquivo_destino = argv

print("Copiando de %s para %s" % (arquivo_origem, arquivo_destino))

in_arquivo = open(arquivo_origem)
in_dados   = in_arquivo.read()

print("O arquivo de origem tem tamanho de %d bytes." % len(in_dados))

print("O arquivo de destino existe? %r" % exists(arquivo_destino))

print("Pronto! Aperte ENTER para continuar ou CTRL-C para sair.")
input()

out_arquivo = open(arquivo_destino, 'w')
out_arquivo.write(in_dados)

print("Tudo está pronto...")

out_arquivo.close()
in_arquivo.close()
