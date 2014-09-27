pessoas = 30
carros = 40
onibus = 15

if carros  > pessoas:
    print("Nós devemos ir de carro.")
elif carros < pessoas:
    print("Nós não devemos ir de carro.")
else:
    print("Nós não podemos decidir.")

if onibus > carros:
    print("Há muitos onibus.")
elif onibus < carros:
    print("Talvez nós possamos ir de ônibus.")
else:
    print("Nós não podemos decidir.")

if pessoas > onibus:
    print("Certo, vamos pegar ônibus.")
else:
    print("Legal, vamos ficar em casa.")
