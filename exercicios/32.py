print("Você entra em um quarto escuro com duas portas. Por onde você quer ir \
      porta #1 ou porta #2?")

porta = input(">>> ")


if porta == '1':
    print("Tem um urso gigante comendo um bolo. O que você faz?")
    print("1. Pegar o bolo")
    print("2. Gritar com o urso.")

    urso = input(">>> ")

    if urso == '1':
        print("O urso come a sua cara. Bom trabalho.")
    elif urso == '2':
        print("O usro come as suas pernas. Bom trabalho.")
    else:
        print("Bom, %s é provavelmente melhor. O urso foge." % urso)
elif porta == '2':
    print("Você olha para um abismo sem fim")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies")

    insanidade = input(">>> ")

    if insanidade == "1" or insanidade == "2":
        print("Your body survives powered by a mind of jello. Good job")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job")
else:
    print("Você tropeça cai sobre uma faca e morre. Bom trabalho.")
