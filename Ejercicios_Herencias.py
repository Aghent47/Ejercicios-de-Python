class Calculator:
    pass
    def __init__(self,numero):
        self.num = numero
        self.datos = [0 for i in  range(numero)]

    def ingresar_Dato(self):
        self.datos = [int(input("ingresar datos "+str(i+1)+ " = ")) for i in range(self.num)]#delimitando cuantos datos quiero ingresar

#Operaciones Basicas
class OperationsBasic(Calculator):
    pass
    def __init__(self):
        Calculator.__init__(self,2)
    
    def sumar(self):#metodo para sumar
        numberOne,numberTwo, = self.datos 
        result = numberOne + numberTwo
        print('El resulado es: ',result)
    
    def restar(self):#metodo para restar
        numberOne,numberTwo, = self.datos 
        result = numberOne - numberTwo
        print('El resulado es: ',result)
    
    def mult(self):#metodo para multiplicar
        numberOne,numberTwo, = self.datos 
        result = numberOne * numberTwo
        print('El resulado es: ',result)

    def div(self):#metodo para dividir
        numberOne,numberTwo, = self.datos 
        result = numberOne / numberTwo
        print('El resulado es: ',result)

#Operaciones avanzadas
class Raiz(Calculator):
    pass
    def __init__(self):
        Calculator.__init__(self,1)
    
    def cuadrada(self):
        import math
        numberOne, = self.datos
        print('el resutado: ',math.sqrt(numberOne))

ope = OperationsBasic()#creando object y vamos a trabajar con la clase operationsBasic
print(ope.ingresar_Dato())
print(ope.sumar())

ope2 = Raiz()
print(ope2.ingresar_Dato())#creando objecto para trabajar con la clase Raiz y el metodo cuadrada
print(ope2.cuadrada())

objecto = OperationsBasic()

#funciones integradas
print(isinstance(objecto,OperationsBasic))#comprobrar si trabajamos con la funcion indicada
print(issubclass(Calculator,OperationsBasic))
print(issubclass(OperationsBasic,Calculator))#comprobrar si la clase OperationsBasic es una Subclase de Calculator


