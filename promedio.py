print("\x1bc")
# 90-100 = A
# 80-89 = B
# 75-79 = C
# 70-74 = D
# 00-70 = F  OR  # 00-49 = F

while True:
    print("\nDigite los valores: ")
    a = int(input("Assistencia: "))
    b = int(input("1st parcial: "))
    c = int(input("Practica: "))
    d = int(input("Examen final: "))

    val = (a+b+c+d)
    if (val >= 90):
        print("\n Nota Final: A")
    elif(val >= 80):
        print("\n Nota Final: B")
    elif(val >= 75):
        print("\n Nota Final: C")
    elif(val >= 70):
        print("\n Nota Final: D")
    elif(val < 70):
        print("\n Nota Final: F")
    else:
        print("sorry ty again")


###################################################################

# # import statistics

# # promedio = [4, 12]

# # x = statistics.mean(promedio)

# # print("El promedio entre", promedio, "es :", int(x))


# import statistics

# # list of positive integer numbers
# data1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# x = statistics.mean(data1)
# y = statistics.mean(data2)

# # Printing the mean
# print("Mean 1 is :", x)
# print("Mean 2 is :", y)
