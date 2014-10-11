import json
import urllib.request as request

def get_autenticacao():
    arquivo_credenciais = open('credenciais.json')
    autenticacao        = json.load(arquivo_credenciais)
    arquivo_credenciais.close()

    usuario = autenticacao['usuario']
    senha   = autenticacao['senha']
    
    return usuario + ':' + senha

def autentica_proxy():
    autenticacao = get_autenticacao()

    url    = r'http://' + autenticacao + '@proxy.unipam.edu.br:3128'
    
    proxy  = request.ProxyHandler({'http': url})
    auth   = request.HTTPBasicAuthHandler()
    opener = request.build_opener(proxy, auth, request.HTTPHandler)
    
    request.install_opener(opener)

    return request

def get_pagina(pesquisa):
    #request = autentica_proxy()
    #url = 'http://pt.wikipedia.org/wiki/' + pesquisa
    url = 'http://pt.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exchars=500&exlimit=1&explaintext=&exsectionformat=plain&titles=' + pesquisa

    conteudo = request.urlopen(url)

    return conteudo.read().decode('utf-8')

def iniciar():
    pesquisa = input('Digite o termo de pesquisa: ')
    conteudo = get_pagina(pesquisa)
    
    conteudo_json = json.loads(conteudo)
    
    paginas = conteudo_json['query']['pages']
    
    for i in paginas:
    	extract = paginas[ i ][ 'extract' ]
    	
    	print(extract)
    
iniciar()
