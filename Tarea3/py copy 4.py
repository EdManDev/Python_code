print("\033c")


print("dos numero y su division, error si el divisor es igual a cero")

num_1 = int(input("digite num_1: "))
num_2 = int(input("digite num_2: "))
res = num_1//num_2

if(res > 1):
    print("resultado es: ", res)
else:
    print("error!")
