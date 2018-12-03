print("calcuo del interes locales\n")

tasa_interes = int(input("ingrese la tasa de interes: "))

if tasa_interes < 500:
    print("la tasa es de 2%")
elif tasa_interes == 500:
    print("la tasa es 5.5%")
else:
    print("la tasa es 9%")

