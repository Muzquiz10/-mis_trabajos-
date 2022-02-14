#### JUEGO NUMERO ALEATORIO ###

vidas = 2
import random
n_aleatorio = random.randint(1,5)
print(n_aleatorio)


while vidas > 0:
	jugador = int(input("Inserte un número: "))
	if jugador != n_aleatorio:
		vidas = vidas - 1

	elif jugador == n_aleatorio:
		print("You win")
		break

if vidas == 0:
	print("You lose")