print("\033c")

print('en un estasamiento se cobra 2.5 por hora')

horas = int(input('Ingrese la cantidad de horas: '))

minutos = 30  # int(input('Ingrese la cantidad de minutos: '))
fract = minutos / 60
tiempo = fract + horas
pago = tiempo * 2.5

print('Usted ingreses:', horas, ', El importe a pagar es', pago, 'pesos')
