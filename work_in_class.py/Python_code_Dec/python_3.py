print("\033c")


while True:
    D = float(input("digite al limite: "))
    C = 0
    while (C <= D):
        # for C in range (D):
        C = C+1
        if ((C % 2) == 0):
            print("Pares", C)
        else:
            print("impares", C)
        break
