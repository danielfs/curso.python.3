# importar no shell interativo

def separar_palavras(palavra):
    """Essa função irá separar palavras para nós."""
    palavras = palavra.split()
    return palavras


def ordenar_palavras(palavras):
    """Ordena palavras."""
    return sorted(palavras)


def imprime_primeira_palavra(palavras):
    """Imprime a primeira palavra, depois remove ela da lista"""
    palavra = palavras.pop()
    print(palavra)


def imprime_ultima_palavra(palavras):
    """Imprime a ultima palavra, depois remove ela da lista"""
    palavra = palavras.pop(-1)
    print(palavra)


def ordenar_sentenca(sentenca):
    """Recebe uma sentenca e retorna as palavras ordenadas"""
    palavras = separar_palavras(sentenca)
    return ordenar_palavras(palavras)


def imprime_primeira_e_ultima(sentenca):
    """Imprime a primeira e ultima palavra de uma sentenca."""
    palavras = separar_palavras(sentenca)
    imprime_primeira_palavra(palavras)
    imprime_ultima_palavra(palavras)


def imprime_primeira_e_ultima_ordenada(sentenca):
    """Ordena as palavras e imprime a primeira e ultima palavra"""
    palavras = ordenar_palavras(sentenca)
    imprime_primeira_palavra(palavras)
    imprime_ultima_palavra(palavras)
