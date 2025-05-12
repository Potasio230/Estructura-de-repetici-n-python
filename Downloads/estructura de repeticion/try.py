#Ejercicio 1: Calculadora de Edad
#Crea un programa que:
#Pida la edad al usuario
#Valide que sea un número entero
#Calcule el año de nacimiento
#Maneje posibles errores de entrada

edad = int(input("Ingrese su edad: "))
añoNacimiento = int(input("Ingrese su año de nacimiento"))

if edad > 1950 and añoNacimiento < 2025:
    calculo = edad - añoNacimiento
    print("Tu edad es: ", calculo)

 



