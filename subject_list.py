subject_list=[]

number_of_subject = int(input('ingrese la cantidad de materias: '))

for i in range(number_of_subject):
  subject = input('Ingrese el nombre de la materia '+ str(i+1) + ':')
  subject_list.append(subject)
  student_note = input('Que nota desea para esta materia de 0 a 5:')
  subject_list.append(student_note)

print(subject_list)