print("\033c")
print("division de gupo de Alumnos en A B")
nombre = str(input("inrese tu nombre: "))
sexo = str(input("ingerse el sexo F o M: "))

if(sexo == "F"):
    print("Groupo A")
    print("Nombre", nombre, "anterior N")
else:
    print("Groupo B")
    print("Nombre ", nombre, "posterior M")
