print("\033c")

u = int(input("Digite el universo: "))
c = 1
while (c <= u):
    if (c == 3):
        print("del universo", u, c, "es el mundo de 3")
    else:
        c = c+1
        print(c, "no es el multiples  de 3")
        print("Fin de proceso...\n")
        # print("\t\t\t\tfin de proceso")
