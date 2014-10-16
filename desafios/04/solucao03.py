import json
import urllib.parse   as parse
from curso.conexao import get_pagina_wikipedia

def iniciar():
    pesquisa = input('Digite o termo de pesquisa: ')
    conteudo = get_pagina_wikipedia(parse.quote_plus(pesquisa))
    
    conteudo_json = json.loads(conteudo)
    
    paginas = conteudo_json['query']['pages']
    
    for i in paginas:
    	extract = paginas[ i ][ 'extract' ]
    	
    	print(extract)
    
iniciar()
