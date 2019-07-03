print("\033c")
while True:
    pais = str(input("ingrese un pais: \n"))

    if pais == "rep. dominicana":
        print(pais, "ha sido selecionado y su indice esta 11 088 647 habitante")
    elif pais == "rwanda":
        print(pais, "ha sido selecionado y su indice esta 12 718 198 habitante")
    elif pais == "china":
        print(pais, "ha sido selecionado y su indice esta 12 1 403 500 365 habitante mas poblado del mundo")
    else:
        print("\nningun pais ha sido seleccionado!")
        print("Deseas de regresar de nuevo (si) o (no)!")

        pregunta = str(input())
        if pregunta == "si":
            pais = pais
        else:
            break
