print("\033c")
print("calcula un programa para calcular los salario semanales de unos empleados")

hora=int(input("entroduzca la hora: "))
pago=150*hora
if (hora > 35):
  print("se considera EXTRA!")
  resultado=pago+220
  print("el salario es: ", resultado,"pesos")
else:
  print("hay algo malo")