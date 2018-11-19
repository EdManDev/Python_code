import cmath

A=4
B=2
C=1

sqrt = cmath.sqrt(A+B-C)+100

print('The square root of {0} is: {1:0.3f}'
      .format(A ,sqrt.real))
