print("este progama imprima numero positivo o negativo")


def generateNumber(num):

    mylist = []

    for i in range(num + 1):

        mylist.append(i)

    return mylist

x = generateNumber(4)

print(x)

