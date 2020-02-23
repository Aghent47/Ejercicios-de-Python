class People:
    pass
    
    #Constructor 
    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año

    #Metodos
    def descricion (self):
        return ' {} tiene {} años '.format(self.nombre,self.año)#Retornando funcion Forman Intelligent
    def  comentario(self,frase):
        return ' {} dice: {} '.format(self.nombre,frase)

doctor = People('Neider', 22) #Creamos el object doctor
print(doctor.descricion())
print(doctor.comentario('ESTOY PROGRAMANDO EN PYTHON'))


#modificar atributos
class Email:
    pass
    def  __init__(self):
        self.enviado = False
    def enviar_email(self):
        self.enviado = True

mi_Email = Email()
print(mi_Email.enviado)
mi_Email.enviar_email()#espeificando cual atributo utilizar
print(mi_Email.enviado)
