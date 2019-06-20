herencia = int(input("Ingresar el monto del herencia: "))
hijos = int(input("igresar el numero de hijos"))
repart = 0

if hijos < 4:
  repart = herencia / hijos
  print("cada persona recibira " + str(repart))
elif hijos > 4:
  repart = herencia / 2
  print("el hijo mayor recibe "+ str(repart))
  print("los demas hijos reciben cada uno/a", repart / (hijos - 1))

