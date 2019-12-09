print("\033c")
print("Este Programa muestra el [volumen] de un cilindro dados su (altura y diametro)\n")

altura=int(input("engrese el altura: "))
diametro=int(input("engrese el diametro: "))
pi=3.14
exp = 2
Radio = diametro//2
volumen = pi ** exp * Radio * altura
print("El Resultado es: ", volumen"cm al cubo")
