#ejercicio random
#importamos random para poder seguir
#no puedes nombrar el archivo igual a una libreria pq no funciona
import random
vidaHeroe = 100
vidaMounstro = 100

#para generar un numero aleatorio escribimos: random.randint(rango numérico)
#el heroe ataca
dañoHeroe = random.randint(1, 70)
vidaMounstro -= dañoHeroe
print("El heroe ataca y hace", dañoHeroe, "de daño.")
print("***************************************************************************")
#el mounstro ataca
dañoMounstro = random.randint(1, 70)
vidaHeroe -= dañoMounstro
#interpolacion de variables 
#print(f"El mounstro ataca y hace {dañoMounstro} de daño")
print("El mounstro ataca y hace", dañoMounstro, "de daño")
print("***************************************************************************")

#mostrar vida restante
print("Vida de heroe", vidaHeroe)
print("Vida de heroe", vidaMounstro)

while vidaMounstro >=1 and vidaHeroe >= 1: 

    dañoHeroe = random.randint(1, 20)
    vidaMounstro -= dañoHeroe
    print("El heroe ataca y hace", dañoHeroe, "de daño.")
    print("***************************************************************************")

#el mounstro ataca
    dañoMounstro = random.randint(1, 20)
    vidaHeroe -= dañoMounstro
    print("El mounstro ataca y hace", dañoMounstro, "de daño")
    print("***************************************************************************")

#mostrar vida restante
    print("Vida de heroe", vidaHeroe)
    print("Vida de heroe", vidaMounstro)



#evaluar resultados
if vidaHeroe <= 0 and vidaMounstro <= 0:
    print("Ambos se murieron al mismo tiempo")
elif vidaHeroe <= 0:
    print("El heroe ha caido... El mounstro gana")
elif vidaMounstro <= 0:
    print("El mountro ha caido... El heroe gana")
else:
    print("Ambos siguen en pie, la batalla continuará en otro momento...")