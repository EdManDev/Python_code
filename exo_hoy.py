# print("\033c") 

ht=int(input("digite horas de trabajados: "))
precio_Hora=float(input("digite pago para hora: "))
sb=ht*precio_Hora
afp=sb*0.0281
ars=sb*0.0301
sueldo_neto1=sb-afp-ars

if (sueldo_neto1 > 34685):
    inpuesto_sobre_renta=(sueldo_neto1-34685)*0.15
else:
    inpuesto_sobre_renta=0
print=("Sueldo Final: ", sueldo_neto1 - inpuesto_sobre_renta)