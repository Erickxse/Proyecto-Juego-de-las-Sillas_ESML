Algoritmo j_Sillas
	sillas <- 0
	participantes <- 0
	turnos <- 0
	Definir listaJugadores Como Caracter
	Escribir 'Bienvenido al juego de las Sillas'
	Mientras participantes<=1 Hacer
		Escribir 'Ingrese el numero de participantes'
		Leer participantes
		Si participantes<=1 Entonces
			Escribir 'Debe haber mas de un jugador'
		SiNo
			sillas <- participantes-1
			Escribir 'El juego comienza con ',participantes,' participantes'
			Escribir 'Sillas en juego: ',sillas
		FinSi
	FinMientras
	Dimension listaJugadores[participantes]
	Para x<-1 Hasta participantes Hacer
		Escribir 'Ingrese nombre del Jugador: '
		Leer nombre
		listaJugadores[x] <- nombre
	FinPara
	Escribir 'Empieza la ronda con los siguientes jugadores: '
	Para i<-1 Hasta p Hacer
		Escribir listaJugadores[i]
	FinPara
	m <- participantes-1
	Si sillas>0 Entonces
		Para x<-1 Hasta m Hacer
			turnos <- turnos+1
			Escribir 'Presiona cualquier tecla para continuar...'
			Esperar Tecla
			Escribir 'Empieza el turno ',turnos
			Escribir 'Suena la Musica...'
			Esperar 3 Segundos
			Escribir 'Se detiene la musica...'
			aleat <- azar(participantes)
			rand <- listaJugadores[aleat]
			Esperar 2 Segundos
			Escribir rand,' Se ha quedado sin silla, es descalificado'
			sillas <- sillas-1
			Escribir 'Se quita una Silla...'
			Para iterador<-1 Hasta participantes Hacer
				Si listaJugadores[iterador]==rand Entonces
					listaJugadores[iterador] <- ''
				FinSi
			FinPara
		FinPara
	FinSi
	Si sillas==0 Entonces
		Escribir 'Juego Terminado'
		Escribir 'El Ganador es: ',listaJugadores[0]
	FinSi
FinAlgoritmo
