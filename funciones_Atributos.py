class People:
    edad = 22
    name = "Neider Hernandez"

doctor = People()
print(doctor.name,doctor.edad,"Años")
print('la edad es: ', getattr(doctor,'edad'))

print('El doctor tiene una edad?',hasattr(doctor,'edad')) #es como si fuera una pregunta edad existe como atributo?    
setattr(doctor,'name','Deyber') #cambiar valor del atributo
print('ahora me llamo: ',doctor.name) 

#eliminar un atributo dentro de una clase
#delattr(People,'edad')
#print("la edad es: ",doctor.edad)