nombre=(input("Tu Nombre es: "))
while True:
  num =int(input("\n engrese el valor de tu edad: "))

  if  18 > num:
    print(nombre + " tu edad es menos de 18.")
  else:
    print(" Tu edad es mayor de 18 te entrego a " +nombre+" 1000 pesos")
