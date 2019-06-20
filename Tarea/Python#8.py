print("DETREMINE SI ES PAR O EN CONTRARIO IMPARES Y DIVIDE POR 3")

num = int(input("Ingrese Un Valor: "))

if (num % 2) == 0:
    print("El valor: ", num, " es pares.")
else:
    num = num // 3
    print("El valor: ", num, " es impares (y ya divide por 3 ).")

