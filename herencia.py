#crear una nueva clase a partir de una o clases existentes (clase primaria, segundarias, clases padres, clases hijos)
class Pokemon:
    pass
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descricion(self):
        return ' {} Es un pokemos de tipo: {} '.format(self.nombre,self.tipo)

class Pikachu (Pokemon):
    def ataque(self,tipo_ataque):#este metodo pertenece a la clase Picachu
        return ' {} tipo de ataque {} '.format(self.nombre,tipo_ataque)

class Charmander (Pokemon):
    def ataque(self,tipo_ataque):#este  metodo pertenece a la clase charmander
        return ' {} tipo de ataque {} '.format(self.nombre,tipo_ataque)

newPokemon = Pikachu('shell', 'Fuego ')#declaramos nuestro object de la clase Picachu
newPokemonn = Charmander('Charts','Aire')#declaramos nuestro object de la clase Charmander

print (newPokemon.descricion())#utilizando la el metodo descriccion de la clase padre
print(newPokemon.ataque('QueduraLetal'))#utilzando el metodo ataque tipo_ataque de la clase Picachu 

print (newPokemonn.descricion())#utilizando la el metodo descriccion de la clase padre
print(newPokemonn.ataque('TornadoViolento'))#utilzando el metodo ataque tipo_ataque de la clase Charmander 
