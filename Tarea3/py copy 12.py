print("\033c")
print("determine si int es impar ")

while True:
    num_1 = int(input())
    num = 2

    if(num_1 % num):
        print("no",num_1," es impares!")
    else:
        print("si",num_1," es pares")
