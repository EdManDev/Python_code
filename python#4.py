print('de terminar el importe a pagar por el concepto de estaciones')

valor_a_pagar = float(input('ingrese el valor a pagar: '))
horas = float(input('ingrese la Hora: '))
precio_por_hora = (('el precio dehora sera expresado cada 30mn'))

sub_total = horas * precio_por_hora
descuento = sub_total * 2.5
sueldo = sub_total-descuento

print('El sueldo a pagar de la hora expresado de'+valor_a_pagar+' es de: '+str(sueldo))
