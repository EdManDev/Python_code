print("\033c")

while True:
    num = int(input("Enter a number: "))
    if (num % 2) == 0:
        print(" is Even number", num)
    else:
        print(" is Odd number", num)
