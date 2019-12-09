print("\033c")
print("calcular las necesidades de combustibles para calcular de forma automatizado")

PrecComb=int(input("ingresar precio de combustible: "))
CadVehic=int(input("ingresar precio de cada vehiculo: "))
CombNece=PrecComb*CadVehic
print("\nEl combustible necesario es: ",CombNece,"DOP\n")
