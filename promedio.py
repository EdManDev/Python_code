print("\x1bc")
# 90-100 = A
# 80-89 = B
# 75-79 = C
# 70-74 = D
# 00-70 = F

while True:
    print("\nDigite los valores: ")
    a = int(input("1st parcial: "))
    b = int(input("2nd parcial: "))
    c = int(input("3rd parcial: "))

    val = (a+b+c)
    if (val >= 90):
        print("A")
    elif(val >= 80):
        print("B")
    elif(val >= 75):
        print("C")
    elif(val >= 70):
        print("D")
    elif(val < 70):
        print("F")
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
