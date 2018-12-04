horas =  int(input("Ingrese la cantidad de horas : "))
minutos = int(input("Ingrese la cantidad de minutos : "))

fracH = minutos / 60
tiempo =  fracH + horas
pago = tiempo * 2.5
print("El importe a pagar es ", pago, " pesos")
