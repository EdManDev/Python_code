print("Una tienda que vende pantalones")

pantalones = int(input("ingrese el numero de de cantidad de pantalones: "))

if pantalones == 5:
    print("\nEsto es el precio Normal\n")
elif pantalones == 12:
    print("es el precio de descuento de 15%\n")

elif pantalones > 12:
    print("es el precio de descuento de 30%\n")
# else:
#     print("\nNigun precio han sido selectionado\n")
