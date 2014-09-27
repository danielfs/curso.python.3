from sys import exit


def morrer(causa):
    print(causa, "Bom trabalho!")
    exit(0)


def mina_de_ouro():
    print("Aqui é uma mina de ouro.  Quanto você quer pegar?")
    proximo = input(">>> ")

    if "0" in proximo or "1" in proximo:
        quanto = int(proximo)
    else:
        morrer("Cara, aprenda a digitar números")

    if quanto < 50:
        print("Bom, você não é ganancioso, você venceu.")
        exit(0)
    else:
        morrer("Você é um ganancioso bastardo")


def sala_do_urso():
    print("Tem um urso aqui")
    print("O urso tem um pote de mel")
    print("O urso gordo está em frente a porta.")
    print("Como você vai fazer o urso sair?")
    urso_saiu = False

    while True:
        movimento = input(">>> ")
        if movimento == "pegar o pote de mel":
            morrer("O urso olha para você, te dá uma patada e arranca sua \
                   cara fora")
        elif movimento == "provocar o urso" and not urso_saiu:
            print("O urso saiu de frente da porta. Agora você pode passar.")
            urso_saiu = True
        elif movimento == "provocar o urso" and urso_saiu:
            morrer("O urso fica chateado e mastiga sua perna")
        elif movimento == "abrir porta" and urso_saiu:
            mina_de_ouro()
        else:
            print("Não faço a minima ideia do que seja isso.")


def sala_do_cthulhu():
    print("Você encontra um grande e malvado Cthulhu.")
    print("Se você não sabe o que é um Cthulhu:\
          http://pt.wikipedia.org/wiki/Cthulhu")
    print("Ele olha para você e você fica maluco.")
    print("Você pode fugir (run for your life) ou comer sua cabeça?")
    movimento = input(">>> ")

    if movimento == "fugir":
        iniciar_jogo()
    elif movimento == "comer":
        morrer("Bom, estava saboroso.")
    else:
        sala_do_cthulhu()


def iniciar_jogo():
    print("Você está em uma sala escura. Tem uma porta na esquerda e direita")
    print("Qual delas você quer abir?")
    movimento = input(">>> ")

    if movimento == "esquerda":
        sala_do_urso()
    elif movimento == "direita":
        sala_do_cthulhu()
    else:
        morrer("Você tropeça pela sala até morrer de fome.")


iniciar_jogo()
