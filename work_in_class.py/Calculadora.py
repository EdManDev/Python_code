# print("digite la tabla de multiplication")
print("\033c")


signos = (
    input("\nEngrese Un Signo De Operador como: +  -  *  / :  \n\n"))

while True:
    print("\n\nEngrese Dos Numero\n")
    num1 = int(input("INGRESE UN NUMERO: "))
    num2 = int(input("ingrese otro : "))

    if (signos == "+"):
        print("El Resulado es igual a:", num1+num2)
    elif (signos == "-"):
        print("El Resulado es igual a:", num1-num2)
    elif (signos == "*"):
        print("El Resulado es igual a:", num1*num2)
    elif (signos == "/"):
        print("El Resulado es igual a:", num1/num2)
    else:
        print("N/A")



        


# if (A * 1):
#     print("4 x 1 es igual a", A)
# elif(A * 2):
#     print("4 x 2 es igual a", A)
# elif(A * 3):
#     print("4 x 3 es igual a", A)
# elif(A * 4):
#     print("4 x 4 es igual a", A)
# elif(A * 5):
#     print("4 x 5 es igual a", A)
# elif(A * 6):
#     print("4 x 6 es igual a", A)
# elif(A * 7):
#     print("4 x 7 es igual a", A)
# elif(A * 8):
#     print("4 x 8 es igual a", A)
# elif(A * 9):
#     print("4 x 9 es igual a", A)
# elif(A * 10):
#     print("4 x 10 es igual a", A)
# else:
#     print("N/A")
