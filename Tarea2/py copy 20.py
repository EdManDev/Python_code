print("\033c")
print("en una libreria han puesoto oferta la vena de cuaderno")

compra = int(input("ingrese el valor de compra: "))

if compra == 12:
    print("regalo niguno")
elif compra < 24:
    print("1 - josue para 4 cuaderno")
elif compra < 36:
    print("2 - Luis por cada 4 cuaderno")
elif compra == 36:
    print("3 - Nelson por cada 4 cuaderno")
