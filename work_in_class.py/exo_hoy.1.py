print("\033c")
while True:
    v = input("digite el nombre del caro: \n")
    if v == "t" or v == "T":
        print("Toyota")
    elif v == "m" or v == "M":
        print("Maza")
    elif v == "n" or v == "N":
        print("Nisan")
    else:
        print("N/A")
