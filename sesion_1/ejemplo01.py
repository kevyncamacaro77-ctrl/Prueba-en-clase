##Ejemplo de Python para Formacion complementaria
x=5
y=10
print ("El valor de 5 * 10 es: ",x * y)
print ("realizado")

nombre = input("coloca tu primer nombre ")
apellido = input("coloca apellido ")

print ("El nombre completo es: " + nombre + " " + apellido )

edad = int(input ("ingrese su edad "))

total = edad + 1500
print ( total )

if ( edad > 18 ):
    print(" Puede entrar al cine Adulto ")
else:
    print ("---- !!!!! OJO !!!!! ----")


""" Otra cosa"""

"""Funciones simples con parametros y retorno."""

def saludar(nombre):
    """""Retorna un saludo simple."""
    return f"Hola, {nombre}"

saludar(nombre)
