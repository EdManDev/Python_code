print("\033c")
# print("\x1bc")

print("este programa imprima ano de 2 hermano")
while True:
    cuantidad = int(input("ingresar los numeros de los hilos: "))
    hijos = 4
    los_demas = hijos / hijos

    if cuantidad <= hijos:
        print(
            "la cuantidad es: ",
            cuantidad,
            " mas le tocara al Hermano  mayor ",
            los_demas,
        )
    else:
        print("la cuantidad es: ", cuantidad, "menos que ", hijos)
        # print("la cuantidad es: ", hijos, "que es mas grande que", cuantidad)
