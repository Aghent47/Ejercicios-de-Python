''' Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá cumplir con los siguientes criterios de aceptación:
El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
El nombre de usuario debe ser alfanumérico.
Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras y números".
Nombre de usuario válido, retorna True '''


class Users(object):        
    def validacion(self,nombre_r):
        if len(nombre_r) >= 6 and len(nombre_r) <= 12 and nombre_r.isalnum() == True :
            self.nameUsers = nombre_r
            return True
            
        elif len(nombre_r) < 6:
            print("El nombre debe tener almenos 6 caracteres!!")
        if len(nombre_r ) > 12:
            print("El nombre debe tener maximo 12 caracteres!!")
        elif nombre_r.isalnum() == False:
            print("El nombre debe contener solo letras y/o numeros")

objecto = Users()
nombre = str(input("Ingrese su nombre: "))
print(objecto.validacion(nombre))
