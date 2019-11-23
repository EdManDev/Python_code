print("\033c")

while True:
    print("en un estasamiento se cobra 20.00 por hora")

    horas = int(input("Ingrese la cantidad de horas: "))

    minutos = 5

    if minutos < horas:
        fract = minutos / 60
        tiempo = fract + horas
        pago = tiempo * 20.00
        print(
            "Usted ingreses:",
            horas,
            "horas, El importe a pagar es %.2f" % (pago),
            "Pesos\n",
        )
        pass
    else:
        print("es incorrecto \n")

