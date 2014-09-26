print("Vamos praticar um pouco de tudo.")
print("Você precisa conhecer sobre caracteres de escape com \\ como \' aspas  \n nova linha e \t tabulução")


poema = """
\tBatatinha
Batatinha quando nasce espalha a rama pelo chão.
Depois que eu aprendi Python ...
"""

print("-" * 15)
print(poema)
print("-" * 15)

cinco = 10 - 2 + 3 - 6  # pemdas - esquerda -> direita
print("Isso deve ser cinco: %s" % cinco)

def formula_secreta(materia_prima):
    jujubas = materia_prima * 500
    potes = jujubas / 1000
    fardo = potes / 100
    return jujubas, potes, fardo


ponto_inicial = 10000
jujubas, potes, fardos = formula_secreta(ponto_inicial)

print("Vamos iniciar com: %d" % ponto_inicial)
print("Nós temos %d jujubas, %d potes, fardos %d." % (jujubas, potes, fardos))

ponto_inicial = ponto_inicial / 10

print("Vamos iniciar com: %d" % ponto_inicial)
print("Nós temos %d jujubas, %d potes, fardos %d." % formula_secreta(ponto_inicial))
