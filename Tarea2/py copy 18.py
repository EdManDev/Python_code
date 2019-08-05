print("\033c")

tuplas=(1,2,3,4)
i=0

while i > 0:
  if tuplas[i] % 2 > 0:
    result = tuplas[i] + 6
    print(result)
  i=i+1