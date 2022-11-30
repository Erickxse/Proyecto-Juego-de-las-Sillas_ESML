"""
El Juego o Baile de las Sillas, es un juego Tradicional que se lo practica en las fiestas
infantiles o Fiestas Familiares en Ecuador, se basa en un numero determinado
de jugadores al rededor de una cantidad de sillas menor en menos una a la cantidad
de jugadores. Los jugadores se ubican en ruedo al rededor de las sillas, una tercera
persona sera la encargada de reproducir la musica mientras los jugadores rodean
las sillas bailando, cuando la musica sea detenida, los jugadores deberan alcanzar una silla.
y sentarse en ella. Aquel jugador que no logre tener una silla, sera descalificado y a la 
vez el numero de sillas se reducira en uno.


El codigo simula el Juego de la Silla, teniendo en cuenta una lista de 
un n numero de participantes
"""
import random as rd
import time
#Inicializar Variables de Valor de Participantes y Turnos
p = 0
turnos = 0
listaJugadores = []
#Se inicializa una lista Vacia, para posteriormente almacenar los nombres de los jugadores
print("Bienvenido al Juego de las Sillas")
#Se solicita el numero de Jugadores con un bucle condicional While
while p<=1:
    participantes = input("Ingrese el numero de participantes: ")
    p = int(participantes) #cast de str a int

    if p<=1:
#Si el numero de Jugadores es menor o igual a 1 no se puede jugar por lo que seguira pidiendo otro numero mayor 
        print("Debe haber mas de un jugador")
 #Si el numero de Jugadores introducidos es mayor a 1 se define el numero de sillas y se imprime cantidad de jugadores y sillas       
    else:
        s = p-1
        #Variable para almacenar la cantidad de sillas (siempre sera menor a uno en la cantidad de jugadores)
        print("El juego empieza con ",p," participantes")
        print("Sillas en juego: " ,s)
        #Mensaje de numero de participantes y Sillas

#Ciclo repetitivo For para solicitar el ingreso de Nombres de Jugadores 
for x in range(p):
    #El ciclo esta controlado por el numero de jugadores (p) Ingresado anteriormente
    nombre = str(input("Ingrese Nombre de Jugador: ")) #En cada iteracion se solicita un nombre de Jugador
    #Cada Nombre se va almacenando en la Lista vacia inicializada 
    listaJugadores.append(nombre) #Va almacenando los nombres en la ultima posicion libre 
    
print("Empieza la Ronda con los siguientes jugadores: \n")
print(listaJugadores)
#Se muestra en pantalla la Lista con los participantes de la ronda

largo = int(len(listaJugadores)) #Se obtiene la longuiotud de la lista y se almacena en una variable

#Inicializamos un ciclo if para cuando el numero de sillas sea mayor que 0
if s>0:
    for x in range(largo-1): #Restamos en 1 la longuitud del vector porque la condicion del juego es que debe quedar un ganador
        #por tanto tambien debe quedar un elemento en el vector
        turnos+=1 #en cada iteracion avanzara un turno
        #Mensajes de interaccion por turnos
        input("Presiona cualquier tecla para continuar..")
        print("Empieza el Turno ",turnos)
        print("Suena La Musica...")
        time.sleep(3)
        print("Se detiene la Musica...")
        #Utilizando la funcion choice de la biblioteca random se selecciona un elemento al azar de la lista de jugadores
        azar = rd.choice(listaJugadores)
        time.sleep(2)
        #dicho elemento elegido o jugador elegido sera el descalificado en ese turno
        print(azar, " Se ha quedado sin silla, es descalificado") #mensaje de Descalificado
        listaJugadores.remove(azar) #se remueve el elemento del vector utilizando su valor en string
        print("Se quita una silla...")
        s-=1 #Se resta una silla por cada turno 
        time.sleep(2)
        print("Participantes restantes: ",len(listaJugadores)) 
        print("Sillas restantes: ",s) 
        #Se imprime por pantalla el numero de jugadores y sillas restantes

#Ciclo if que se cumple cuando el valor de las sillas alcanza su valor de 0
if s == 0:
    print("____________________")
    print("Juego Terminado") #Cuando las sillas llegan a 0 significa que se termino el juego
    #Por tanto se muestra al ganador de la ronda
    print("EL GANADOR ES: ", listaJugadores[0])

