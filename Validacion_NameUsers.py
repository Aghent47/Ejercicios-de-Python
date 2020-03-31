class Users(object):        
    def validacion(self,nombre_r):
        if len(nombre_r) >= 6 and len(nombre_r) <= 12:
            self.nameUsers = nombre_r
            print("Nombre Valido!!")
        else:
            return print("Error Intenelo de nuevo!!!")

            
objecto = Users()
nombre = str(input("Ingrese su nombre: "))
print(objecto.validacion(nombre))
