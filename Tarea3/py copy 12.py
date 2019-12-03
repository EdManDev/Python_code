print("\033c")
print("determine si int es impar ")

while True:
    num_1 = int(input("#1: "))
    num = 2

    if(num_1 % num):
        res = num_1 % num
        print("numero es pares y el resultado es: ", res)
    else:
        print("no. es impares!")
