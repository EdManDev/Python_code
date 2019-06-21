print('\x1bc')


while True:
    name = str(input("\nenter your name: "))
    print("Are you busy", name, "? ")
    response = str(input())
    if response == "yes":
        print("ok you should take a break")
    else:
        print("ok good bye", name)
