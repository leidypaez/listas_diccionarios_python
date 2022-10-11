subject=int(input("ingrese la cantidad de materias que cursa = "))

a = []
i = int(0)
while(i < subject):
  name_subject = str(input("ingrese el nombre de la materia "))
  a.insert(i, name_subject)
  i = i + 1
  
print("que nota espera obtener en cada materia en el primer corte:")
grades = []

for i in range(len(a)):
    while True:
      notes_string = input("nota de " + a[i] + " : ")
      notes_string = notes_string.replace(',','.')  
      note = float(notes_string)
      if note > 5 or note < 0:
        print("ingrese una nota valida")
      else:
        grades.append(note)
        break

print(grades)