## Funcion def

def saludar():
    print("Hola Mundo")

saludar()

#############################################################
##Sin argumento y sin retorno (return) retorna a la funcion

def sumar():
    a=int(input(("Ingrese valor 1>> ")))
    b=int(input(("Ingrese valor 2>> ")))
    c=a+b
    return c
s=sumar()
print(s)

#############################################################
## Con argumento y con retorno

def sumar2(a,b):
    d=e+f
    print(f'La suma de {f} + {e} = {d}')
    return b

e=int(input("ingrese valor 1>> "))
f=int(input("Ingrese valor 2>> "))

s2=sumar2(e,f)
print(s2)

#############################################################

def varios_valores(*args):
    print(type(args))

varios_valores(1,4.5,'juan')

#############################################################
##(Type= Da el tipo de dato)

def varios_revoluciones():
    return 1,4.5,'juan'

z = varios_revoluciones()
print(type(z))

#############################################################
##Resta y (None) sirve para validar 

def resta(a=None, b=None):
    if a == None or b == None:
        print(("Error, Faltan parametros a la funcion"))
        return
    return a - b

resta()

#############################################################
##Calculo

def calculo(precio, descuento):
    return precio - (precio * descuento /100)

datos = [10000, 10]
print("El monto final a pagar es: ",calculo(*datos))