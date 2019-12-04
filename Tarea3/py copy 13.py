print("\033c")
print("elevar al cuadrado un mumro si es par y al cubo si es impar")

num = int(input("Enter a number: "))

if (num % 2) :
    num = num * 2
    print(num, "es impares")
else:
    num = num * 3
    print(num, "es pares")
