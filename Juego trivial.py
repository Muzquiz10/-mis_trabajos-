#### Juego trivial
#  Crear pantalla para seleccionar opciones

"""import random

lista = ["¿Que pintor nació en España: Picasso o Matisse?","¿Cuántos días tiene febrero en 2022?"]
lista_random = random.choice(lista)
print(lista_random)"""

print("¿Que pintor nació en España: Picasso o Matisse?" )

#res_correcta = "Picasso"

Quesitos = 0

respuesta = str(input("Su respuesta es: "))

#if res_correcta == respuesta:
	#print("Correcto, ganas un quesito")
	#Quesitos = Quesitos + 1
if respuesta == "Picasso":
	print("Correcto")
	Quesitos = Quesitos + 1

else:
	print("Pierdes")

#elif respuesta != res_correcta:
	#print("Ohh, no es correcto")


print(Quesitos)

print("¿Cuántos días tiene febrero en 2022?")

#res_correcta_1 = 28

respuesta = int(input("Su respuesta es: "))

if respuesta == 28:
	print("Correcto")
	Quesitos = Quesitos + 1

else: 
	print("Incorrecto")
#if res_correcta_1 == respuesta_2:
	#print("Correcto, ganas otro quesito")
	#Quesitos = Quesitos + 1

#elif respuesta_2 != res_correcta_1:
	#print("Loser")

print(Quesitos)





