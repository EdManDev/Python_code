print("\033c")
print("este programa va determinar el importe a pagar por concepto de estacionamiento")

nombre = str(input('ingrese el nombre del impleado: '))
horas = float(input('ingrese la hora de trabajadores: '))
precio_por_hora = float(input('ingrese la hora del trabajado: '))

sub_total = horas*precio_por_hora
descuento = sub_total*0.07
sueldo = sub_total-descuento

print('El sueldo de los impleado que es ' +nombre+' es de: '+str(sueldo))