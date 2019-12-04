print("\033c")
# NB:

print("indican el tipo de triangulo:\n (1)ISOCELE \n (2)EQUILATERO \n (3)ESCALENO\n")

opt = int(input("Elige un numero: "))

num = 10

a= 4

b= 2

h= 1

l= 8

val_sqrt = 0.5

sqrt = a * val_sqrt 

if(opt==1):
  x = b *2 // 4
  t = b * sqrt - x
  print("isocel: ",t )
elif(opt==2):
  t = val_sqrt * 3 // 4 * a * 2
  print("equilatero: ",t)
elif(opt==3):
  t = b * h // 2
  print("ecaleno: ",t)
else:
  print("hay un error")
