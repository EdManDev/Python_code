print("\033c")
print("Tributar un determinado de impuesto.")

while True:
    edad = int(input("\n\ningrese la edad: "))
    mensual = int(input("cuanto tienes: "))
    precio = 50000
    mayor_edad = 16

    if(edad > mayor_edad):
        if(mensual >= precio):
            print("ahora todo es correcto para tributar ✅")
        else:
            print("tu dinero no es suficiente❗", mensual)
    else:
        print(edad, "debe tener mayor que 16 de edad ❌")
