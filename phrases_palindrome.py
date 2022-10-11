phrase1=str(input("ingrese una frase para determinar si es un palindromo"))

phrase1=phrase1.lower()

phrase1=phrase1.replace(' ','')

phrase1List=list(phrase1)

phrase2List=phrase1List.copy()

phrase2List.reverse()

print(phrase1List)

print(phrase2List)

if phrase1List == phrase2List:
  print("es palindromo")
else:
  print("no es palindromo")