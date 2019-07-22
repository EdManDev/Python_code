print("\033c")
print(" ")
import statistics


num = int(input("ingrese un numero entero: "))
if num <= 10:
    print("Si! el valor", num, "es menos que 10 esta bien ")
else:
    while True:
        num = int(input("No! esta bien ingrese de nuevo: "))
        if num <= 10:
            print("Si! el valor", num, "es menos que 10 esta bien ")
            promedio = 0

            promedio = [4, 12]

            x = statistics.mean(promedio)

            print("El promedio entre", promedio, "es =", int(x))
            break
