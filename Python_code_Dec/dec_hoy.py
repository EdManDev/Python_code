print("\033c")

# lista=[1,2,3,"pollo"]
# lista.append("chicken")
# lista.insert(3,"plato de")
# print(lista,"  \n\n" )

b
print("a -> Agregar:\ni -> Insertar:\nB -> Buscar: ")
var=str(input("digite: "))
if(var == "a"):
  v=str(input("digite el valor a agregar: "))
  l.append(v)
elif(var == "i"):
  v=str(input("digite el valor a insertar: "))
  p=int(input("digite la posicion a colocar: "))
  l.insert(p,v)
elif(var == "b"):
  p=int(input("digite la posicion a buscar: "))
  print(l[p])
else:
  print("error")