print("\033c")
print("\nEste programa va imprimir letra Vocale , semivocales o,consonante")

while True:
  a = input("\n\n Enter a un caracter: ")

  if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
      print(a, "es un Vocale")
  elif a == "y" or "Y":
      print(a, "es un semivocales")
  elif a:
      print(a, "es un consonate")
  else:
      print(a, "N/A")
