import sys; import re
class Cadena:
    pass
    def __init__(self,patron):
        self.patron = patron

    def validarCoincidencia(self,cadena):#Me
        #6x^2-3y+3
        e_Regular = re.compile(r"[+|\-]?[1-9](\d)*(X|x)\^2(\+|\-)[1-9](\d)*(Y|y)[+|\-]([0-9]+)$")
        if e_Regular.match(cadena):
            print("Valido :) ")
            print(e_Regular.match(cadena))
        else:
            print("invalido!!!!")
            print(e_Regular.match(cadena))
try:
    cadena = Cadena(sys.argv[1])
    cadena.validarCoincidencia(cadena.patron)
except:
    print ("Error inesperado!!!!")