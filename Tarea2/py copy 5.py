print("\033c")
print("\nEste programa va imprimir letra Vocale , semivocales o,consonante")

while True:
    caracter = input("\n\n entrar  un caracter: ")

    if (
        caracter == "a"
        or caracter == "e"
        or caracter == "i"
        or caracter == "o"
        or caracter == "u"
    ):
        print(caracter, "es un Vocale")
    elif caracter == "y":
        print(caracter, "es un semivocales")
    else:
        print(caracter, "es un consonate")
