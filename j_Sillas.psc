Algoritmo j_Sillas
	s<-0;
	p<-0;
	turnos<-0;
	Definir listaJugadores Como Caracter;
	Escribir "Bienvenido al juego de las Sillas";
	
	Mientras p<=1 Hacer
		Escribir "Ingrese el numero de participantes"
		Leer p;
		Si p<=1 Entonces
			Escribir "Debe haber mas de un jugador"
		SiNo
			s<-p-1;
			Escribir "El juego comienza con ", p, " participantes"
			Escribir "Sillas en juego: ",s
		Fin Si
	FinMientras
	Dimension listaJugadores[p];
	
	Para x<-1 Hasta p Con Paso 1 Hacer
		Escribir "Ingrese nombre del Jugador: "
		Leer nombre;
		listaJugadores[x]<-nombre;
	Fin Para
	
	Escribir "Empieza la ronda con los siguientes jugadores: "
	Para i<-1 Hasta p Con Paso 1 Hacer
		Escribir listaJugadores[i]
	FinPara
	m<-p-1;
	Si s>0 Entonces
		Para x<-1 Hasta m Con Paso 1 Hacer
			turnos<-turnos+1;
			Escribir "Presiona cualquier tecla para continuar..."
			Esperar Tecla
			Escribir "Empieza el turno ", turnos
			Escribir "Suena la Musica..."
			Esperar 3 Segundos
			Escribir "Se detiene la musica..."
			aleat<-azar(p)
			rand<-listaJugadores[aleat]
			Esperar 2 Segundos
			Escribir rand, " Se ha quedado sin silla, es descalificado"
			s<-s-1;
			Escribir "Se quita una Silla..."
			Para iterador <- 1 Hasta p Con Paso 1 Hacer
				Si listaJugadores[iterador] == rand Entonces
					listaJugadores[iterador]<-''
				FinSi
			FinPara
		Fin Para
	Fin Si
	Si s==0 Entonces
		Escribir "Juego Terminado"
		Escribir "El Ganador es: ", listaJugadores[0] 
	FinSi
FinAlgoritmo
