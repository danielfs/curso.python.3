import re
import os.path
import urllib.request as request


conteudo = ""

if not os.path.isfile('tabela.html'):  # verifica se não existe o arquivo
    url = 'http://globoesporte.globo.com/futebol/brasileirao-serie-a/'
    requisicao = request.urlopen(url)  # realiza a requisição
    conteudo = requisicao.read().decode(
        requisicao.headers.get_content_charset())  # retorna o conteúdo da
                                                   # requisição, corrigindo o
                                                   # problema de codificação.

    conteudo = " ".join(conteudo.split())  # removendo excessos de espaços
                                           # tabulações e quebras de linhas.
    conteudo = conteudo.lower()  # convertendo todos os caracteres para
                                 # letras minusculas.
    with open('tabela.html', 'w') as tabela:  # fazendo cache para economizar
        tabela.write(conteudo)                # recursos.

else:
    conteudo = open('tabela.html').read()  # retorna o conteúdo do arquivo



regex_posicao = re.compile(r'<td rel="grafico-posicao" class="posicao"(.+?)</td>')
regex_clube = re.compile(r'<strong itemprop="name">(.+?)</strong>')
regex_pontos = re.compile(r'<td rel="jogos-pontos" class="coluna-p">(.+?)</td>')

posicoes = regex_posicao.findall(conteudo)
clubes = regex_clube.findall(conteudo)
pontos = regex_pontos.findall(conteudo)

# print(posicoes)
# print(clubes)
# print(pontos)

for posicao, time, pontuacao in zip(posicoes, clubes, pontos):
    # método zip itera sobre listas de mesmo tamanho
    # retornando sempre a mesma posicao das listas
    # [0, 1, 2], [0, 1, 2], [0, 1, 2]
    # (0, 0, 0); (1, 1, 1); (2, 2, 2)
    # posicao = posicao[posicao.find('>') + 1:]  # método 1
    posicao = posicao.split('>')[1]  # método 2
    print("%s - %s: %s" % (posicao, time, pontuacao))