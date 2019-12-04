print("\033c")
print("lea un numero e indique si es par o no")

numero=int(input("ingrese el numero: "))
if(numero %2):
  print(numero," es impares: ")
else:
  print(numero," es pares: ")
