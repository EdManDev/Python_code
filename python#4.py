print('de terminar el importe a pagar por el concepto de estaciones')


valor_pagar = str(input('ingrese el valor a pagar:  '))
horas = float(input('ingrese la Hora: '))
precio_por_hora = float(input('ingrese la hora o fraccion de hora: '))

sub_total = horas*precio_por_hora
descuento = sub_total*0.07
sueldo = sub_total-descuento

print('El sueldo a pagar de la hora expresado de '+valor_pagar+' es de: '+str(sueldo)+' de hora y minuto')
