def adicao(a, b):
    print("Adicionando %d + %d" % (a, b))
    return a + b

def subtracao(a, b):
    print("Subtraindo %d - %d" % (a, b))
    return a - b

def multiplicacao(a, b):
    print("Multiplicando %d * %d" % (a, b))
    return a * b

def divisao(a, b):
    print("Dividindo %d / %d" % (a, b))
    return a / b


print("Vamos fazer um pouco de cálculos matemáticos com funções")

idade = adicao(30, 5)
altura = subtracao(78, 4)
peso = multiplicacao(90, 2)
qi = divisao(100, 2)

print("Idade: %d, Altura: %d, Peso: %d, QI: %d" % (idade, altura, peso, qi))

# Um desafio valendo pontos extras.
desafio = adicao(idade, subtracao(altura, multiplicacao(peso, divisao(qi, 2))))

print("O resultado é:", desafio, "Você pode fazer isso mentalmente?")
