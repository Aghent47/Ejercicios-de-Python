class  Matematica:
    def sumar(self):
        self.n1 = 2
        self.n2 = 3
obt = Matematica()
obt.sumar()
print(obt.n2 + obt.n1)

class Ropa:
    def  __init__(self):
        self.marca = 'Nike'
        self.talla = 'M'
        self.color = 'red'
        super().__init__()

camisa = Ropa()
print(camisa.talla)
print(camisa.marca)

class Phone:
    def __init__(self):
        self.color = 'Rojo'
        self.number = 12131231
        super().__init__()

objeto = Phone()
print(objeto.color)
