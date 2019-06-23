print("\033c")
  
while True:
    v = input("digite el nombre del caro: ")
    if v == "t":
        print("Toyota")
    elif v == "m":
        print("Maza")
    elif v == "h":
        print("Honda")
    elif v == "n":
        print("Nissan")
    else:
        print("N/A")
