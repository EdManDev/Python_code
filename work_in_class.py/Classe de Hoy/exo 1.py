print('\x1bc')
# en una tupla numerica entera sumar 5 a los valoress impares que esten en ella 
t1=(1,2,3,4,5,6,7,8,9,10)
i=0
while i<5:
    if (t1 [i] % 2 > 0):
        b= t1[i] + 5
        print(b)
    i=i+1
