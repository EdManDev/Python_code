print('de terminar el importe a pagar por el concepto de estaciones...')


valor_pagar = str(input('ingrese el valor a pagar:  '))
horas = float(input('ingrese la Hora: '))
fraccion_hora = float(2.5)

sub_total = horas*fraccion_hora



print('El sueldo a pagar de la hora expresado es '+valor_pagar+' que es: '+str(sub_total)+' DOP por h/mn')
