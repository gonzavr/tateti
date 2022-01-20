#TA - TE - TI

import random

def dibujarTablero(tablero):
	#dibuja el tablero recibido como argumento
	#tablero es una lista de 10 cadenas,en la pizarra ignora el 0
	
	print('	|	|')
	print(''+ tablero[7] +' | '+tablero[8] +' | '+tablero[9])
	print('	|	|')
	print('--------')
	print('	|	|')
	print(''+ tablero[4] +' | '+tablero[5] +' | '+tablero[6])
	print('	|	|')
	print('--------')
	print('	|	|')
	print(''+ tablero[1] +' | '+tablero[2] +' | '+tablero[3])
	print('	|	|')

def ingresaLetraJugador():
	#permite al jugador typear que letra desea ser.
	#devuelve una lista con letras de los jugadores del primer item, y la computadora del segundo
	
	letra = ''
	while not (letra == 'X' or letra == 'O'):
		print ('¿Que desea ser X o O ?')
		letra=input().upper()
		
		#el primer elemento de la lista es la letra del jugador, el segundo es la letra de la compu
	if letra == 'X':
		return['X','O']
	else:
		return['O','X']

def quienComienza():
	#elije al azar que jugador comienza
	if random.randint(0,1) == 0:
		return 'La Computadora'
	else:
		return 'El Jugador'

def jugarDeNuevo():
	#esta Funcion Devuelve True (verdadero) si el jugador desea volver a jugar, de lo contrario devuelve (Falso).
	print('¿Deseas Volver a Jugar ?(Si/No)')
	return input().lower().startswith('s')
	
def hacerJugada(tablero, letra, jugada):
	tablero[jugada] = letra

def esGanador(ta,le):
# Dado un tablero y la letra de un jugador, devuelve True (verdadero) si el mismo ha ganado. 
#Utilizamos reemplazamos tablero por ta y letra por le para no escribir tanto.
	return((ta[7] == le and ta[8] == le and ta[6] == le) or # horizontal superior
	(ta[4] == le and ta[5] == le and ta[6] == le) or #horiental inferior
	(ta[1] == le and ta[2] == le and ta[3] == le) or # vertical izquierda
	(ta[7] == le and ta[4] == le and ta[1] == le) or # vertical medio
	(ta[8] == le and ta[5] == le and ta[2] == le) or # vertical derecha
	(ta[9] == le and ta[6] == le and ta[3] == le) or # diagonal
	(ta[7] == le and ta[5] == le and ta[3] == le) or # diagonal
	(ta[9] == le and ta[5] == le and ta[1] == le))

def obtenerDuplicadoTablero(tablero):
	#Duplica la Lista del Tablero y Devuelve el Duplicado.
	dupTablero = []
	
	for i in tablero:
		dupTablero.append(i)
	return dupTablero

def hayEspacioLibre(tablero, jugada):
	#Devuelte True si hay espacio para efectuar la jugada en el tablero.
	return tablero[jugada] == ' '
	
def obtenerJugadaJugador(tablero):
	#permite al jugador escribir su jugada.
	jugada = ' '
	while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
		print('¿Cual es Tu proxima Jugada? (1-9)?')
		jugada = input()
		return int(jugada)

def elegirAzarDeLista(tablero, listaJugada):
	#Devuelve una jugada valida en el tablero de la lista recibida.
	#devuelve none si no hay ninguna jugada valida
	jugadasPosibles = []
	for i in listaJugada:
		if hayEspacioLibre(tablero, i):
			jugadasPosibles.append(i)
	
	if len(jugadasPosibles) != 0:
		return random.choice(jugadasPosibles)
	else:
		return None

def obtenerJugadaComputadora(tablero, letraComputadora):
	#dado un tablero y la letra de la computadora, determina que jugada efectuar.
	if letraComputadora == 'X':
		letraJugador = 'O'
	else:
		letraJugador = 'X'
		
	#Aqui Esta nuestro algoritmo para nuestra IA del tateti.
	#primero, verifica si podemos ganar en la proxima jugada.
	for i in range(1,10):
		copia = obtenerDuplicadoTablero(tablero)
		if hayEspacioLibre(copia, i):
			hacerJugada(copia, letraComputadora, i)
			if esGanador(copia, letraComputadora):
				return i
	#Verifica si el jugador podria ganar en su proxima jugada, y lo bloquea

	for i in range(1,10):
		copia = obtenerDuplicadoTablero(tablero)
		if hayEspacioLibre(copia,i):
			hacerJugada(copia,letraJugador,i)
			if esGanador(copia, letraJugador):
				return i
	
	#intenta ocupar una de las esquinas de estar libre
	jugada = elegirAzarDeLista(tablero,[1,3,7,9])
	if jugada != None:
		return jugada
		#de estar libre, intenta ocupar el centro
	if hayEspacioLibre(tablero, 5):
		return 5
	
	#ocupa alguno de los lados.
	return elegirAzarDeLista(tablero,[2,4,6,8])

def tableroCompleto(tablero):
	#devuelve True si cada espacio del Tablero fue ocupado, caso contrario devuelve False.
	for i in range(1,10):
		if hayEspacioLibre(tablero, i):
			return False
	return True

print(' ¡ Bienvenido al TA TE TI ! ')

while True:
	#reseta el tablero
	elTablero = [' ']*10
	letraJugador, letraComputadora = ingresaLetraJugador()
	turno = quienComienza()
	print(turno + ' ira primero. ')
	juegoEnCurso = True
	
	while juegoEnCurso:
		if turno == 'El Jugador':
			#turno del Jugador
			dibujarTablero(elTablero)
			jugada = obtenerJugadaJugador(elTablero)
			hacerJugada(elTablero, letraJugador, jugada)
			
			if esGanador(elTablero, letraJugador):
				dibujarTablero(elTablero)
				print('¡¡¡ Felicidades, has Ganado !!!')
				juegoEnCurso = False
			else:
				if tableroCompleto(elTablero):
					dibujarTablero(elTablero)
					print('¡ Es Un Empate!')
					break
				else:
					turno = 'La Computadora'
		else:
			# Turno de la computadora
			jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
			hacerJugada(elTablero, letraComputadora, jugada)

		if esGanador(elTablero, letraComputadora):
			dibujarTablero(elTablero)
			print('¡La computadora te ha vencido! Has perdido.')
			juegoEnCurso = False
		else:
			if tableroCompleto(elTablero):
				dibujarTablero(elTablero)
				print('¡Es un empate!')
				break
			else:
				turno = 'El jugador'
	if not jugarDeNuevo():
		break
