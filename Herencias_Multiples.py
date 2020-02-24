#La herencia multiple se refiere a la posibilidad de crear una clase a partir de multiples clases superiores.
#Herencias multinivel, caracteristicas de la clase base y la clase derivada se heredan en la nueva derivada.
class Phone:
    def __init__(self):#Constructor
        pass
    def llamar(self):
        print('Llamando...')
    
    def ocupado(self):
        print('ocupado')

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print('Tomando Foto...')
    
class Reproduccion:
    def __init__(self):
        pass
    def reproduccion(self):
        print('Reproduciendo Musica')
    def reproducionVideo(self):
        print('Reproduccioen Videos...')

class Smarphone(Phone,Camara,Reproduccion):#Herencia Multiple
    def __del__(self): #Destructor
        print('Telefono Apagado.')

movil = Smarphone()
print(movil.fotografia())
