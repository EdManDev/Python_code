# print("\033c")

compra = int(input("ingrese el valor del precio: "))
meses = input("ingrese el meses")

if compra == 3:
    print("Diciembre 3%")
elif compra == 5:
    print("octubre 5.5%")
elif compra == 4:
    print("Noviembre 4%")
elif compra == 8:
    print("septiembre 8%")
else:
    print("N/A")
