formatador = "%r %r %r %r"

print( formatador % ( 1, 2, 3, 4 ) )
print( formatador % ( "um", "dois", "três", "quatro" ) )
print( formatador % ( True, False, True, False ) )
print( formatador % ( formatador, formatador, formatador, formatador ) )
print( formatador % (
	"Eu tinha esta coisa.",
	"Que um dia eu poderia digitar certo.",
	"Mas isto não cantava.",
	"Então eu disse boa noite."
) )
