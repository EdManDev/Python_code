print("\033c")
print("")

num_1 = int(input("ingerse un numero 1: "))
num_2 = int(input("ingerse un numero 2: "))
num_3 = int(input("ingerse un numero 3: "))

res=num_1+num_2+num_3
res_final= res//3
var=0
print("el resultado de la media aritmetica: \",res_final)
while res_final > var:
    res_final = res_final - 1
    print ("el resultado final es: ",res_final)