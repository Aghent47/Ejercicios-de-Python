class People:
    edad = 22
    name = "Neider Hernandez"

doctor = People()
print(doctor.name,doctor.edad,"Años")
print('la edad es: ', getattr(doctor,'edad'))

print('El doctor tiene una edad?',hasattr(doctor,'edad'))

