x = "Há %d tipos de pessoas." % 10
binario = "binário"
nao = "não"
y = "Aquelas que sabem %s e aquelas que %s." % ( binario, nao )

print( x )
print( y )

print( "Eu disse: %r." % x )
print( "E também disse: '%s'." % y )

engracado = False
avaliacao_da_piada = "Esta piada não é muito engraçada?! %r"

print( avaliacao_da_piada % engracado )

w = "Este é o lado esquerdo de..."
e = "uma string com um lado direito."

print( w + e )
