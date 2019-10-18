print("\x1bc")

while True:
    print("\ninter value: ")
    a = int(input("val1: "))
    b = int(input("val2: "))
    # c=int(input("val3: "))

    val = (a+b)
    if (val >= 90):
        print(val)
    elif(val <= 80):
        print("B")
    elif(val <= 79):
        print("C")
    else:
        print("no no")
