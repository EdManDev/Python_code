print("\x1bc")


name = str(input("\nENTER YOUR NAME: "))
while True:
    print("-Are you busy", name, "? ")
    response = str(input())
    if response == "yes":
        print("-ok you should take a break", name)
    elif response == "what":
        print("-i said if you Are busy?", name)
        response = response
    elif response == "yes":
        print("-ok you should take a break\n", name)
        name = name
        if response == "ok":
            continue
    else:
        print("ok good bye", name)
        break
