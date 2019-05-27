print("\n\n este programa va imprimir letra Vocale, semivocales,consonante")
while True:

  a = input("Enter a aaracter: ")

  if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
      print(a, "es un Vocale")
  elif a == "y":
      print(a, "es un semivocales")
  else:
      print(a, "es un consonante")
