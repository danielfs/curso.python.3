from sys import argv

script, nome_usuario = argv
prompt = '> '

print("Olá %s, Eu sou o %s script." % (nome_usuario, script))
print("Eu gostaria de lhe fazer algumas perguntas.")
voce_gosta = input("%s, você gosta de mim? " % nome_usuario)
onde_mora = input("Onde você mora, %s? " % nome_usuario)
computador = input("Que tipo de computador você tem? ")

print("""
Certo, você disse %r sobre gostar de mim.
Você mora em %r, mas eu não sei onde fica.
E você tem um computador %r. Bom!
""" % (voce_gosta, onde_mora, computador))
