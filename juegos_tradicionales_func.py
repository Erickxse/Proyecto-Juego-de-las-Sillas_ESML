"""
Descripción:
Simula los juegos tradicionales adaptando sus condiciones y sus estados
estrictamente bajo el uso de condicionales de lógica proposicional. Los juegos seleccionados son Limbo,
El baile de las sillas y Busqueda de pareja.

Autores:
Christopher Amek Bazurto Mora
Erick Sebastian Mora Lara
Anibal Martin Yucailla Padilla

Verisión:
VER.1.1.0
"""
import random as rd
import time
import os

def menuInicial(juegos):
    """
    Es un procedimiento con un bucle for que recorre los elementos del diccionario
    descrito por cada uno de los juegos Tradicionales, mediante la funcion sorted
    se logra que los ekementos se muestren en el orden propuesto:
    ------------
        Recibe un diccionario (juegos) como parametro
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("------------------------------------------\n")
    print("                  BIENVENIDOS              \n")
    print("                TRADITIONAL GAMES         \n")
    print("------------------------------------------\n")
    for clave in sorted(juegos):
        print(f' {clave}) {juegos[clave][0]}')

def eleccion(juegos):
    """
    Es un procedimiento que valida el ingreso de datos en el menu de seleccion
    Se ha validado los numeros del 1 al 4 donde (1-3) corresponde a las opciones
    de juegos y (4) corresponde a salida del programa. Para un valor ajeno se 
    mostrara un mensaje de validacion:
    ------------
        Recibe un diccionario (juegos) como parametro
    
    Retorna:
    ------------
        Retorna una variable (a) de tipo char que indica el valor de entrada escrito por el usuario
    """
    while(a := input('Ingrese el juego: ')) not in juegos:
        print("-----------------------------------------------------------\n")
        print("\nEl juego no esta en la lista \n")
        print("Por favor ingre valores entre 1-3 para seleccionar un juego \n")
        print("-----------------------------------------------------------\n")
    return a

def elegir(juego, juegos):
    """
    Es un procedimiento que recibe una opcion del menu de juegos escrita por el usuario
    en pantalla y ejecuta la opcion elegida correspondiente al diccionario de opciones:
    ------------
        Recibe la opcion seleccionada (juego) y el diccionario (juegos) como parametros
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    juegos[juego][1]()

def generarMenu(juegos, juego_elegido):
    """
    Es un procedimiento que encapsula 3 funciones definidas anteriormente y las ejecuta
    primero muetra el menu en pantalla, luego lee la opcion escrita por el usuario y la valida
    y por ultimo ejecuta la opcion relacionada a la entrada:
    ------------
        Recibe el diccionario (juegos) y la seleccion (juego_elegido) como parametros
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    juego = None
    while juego != juego_elegido:
        menuInicial(juegos)
        juego = eleccion(juegos)
        elegir(juego, juegos)
        print()       

def menuPrincipal():
    """
    Es un procedimiento en el que se define el diccionario con las opciones de los diferentes juegos,
    se han definido 3 opciones y una adicional para salir del programa:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    juegos = {
        '1' : ("Juego 1: LIMBO", juego1),
        '2' : ("Juego 2: JUEGO DE LAS SILLAS", juego2),
        '3' : ("Juego 3: BUSQUEA DE PAREJAS", juego3),
        '4' : ("Salir", salir)
    }

    generarMenu(juegos, '4')
##########################################################################################################
#Funcions para el juego 1 Limbo
##########################################################################################################

def finDeJuego():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al perder el juego
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||         FIN DEL JUEGO       ||\n")
    print("||           PERDISTE          ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||             :C              ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("*************************************\n")
    print("\n")


def nivelUno():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al primer nivel del juego limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||=============================||\n")
    print("||                 __          ||\n")
    print("||                |  |         ||\n")
    print("||                |__|         ||\n")
    print("||               /             ||\n")
    print("||        |_____/              ||\n")
    print("||        _____/               ||\n")
    print("||       |    |                ||\n")
    print("||       |    |                ||\n")
    print("||     __|    |__              ||\n")
    print("*************************************\n")
    print("\n")

def nivelDos():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al segundo nivel del juego limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||=============================||\n")
    print("||                 __ ___      ||\n")
    print("||         |______/  |___|     ||\n")
    print("||          _____/             ||\n")
    print("||         /    /              ||\n")
    print("||        /    /               ||\n")
    print("||     __|    |__              ||\n")
    print("*************************************\n")
    print("\n")

def nivelTres():
    """
    Es un procedimiento que nos muestra una impresión correspondiente al tercer nivel del juego limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("\n")
    print("*************************************\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||                             ||\n")
    print("||=============================||\n")
    print("||           \___________      ||\n")
    print("||        ______|   |____|     ||\n")
    print("||     __|   __|               ||\n")
    print("*************************************\n")
    print("\n")

def reglas():
    """
    Es un procedimiento que nos muestra una impresión correspondiente a las reglas del juego
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("_______________________________________________________________\n")
    print("Este juego contara de 3 preguntas, referenciando a 3 niveles,\n")
    print("si respones una pregunta bien podras pasar la barra del limbo\n")
    print("en caso de que falles una perderas.\n")
    print("_______________________________________________________________\n")

def validador(num):
    """
    Es un procedimiento que nos determina si un dato ingresado(numero) es un digito
    si lo es retorna un True(Verdadero) en caso de que no lo sea retorna un False(Falso)
    Parametros:
    ------------
        Tiene  un parametro de entrada (num)
    
    Retorna:
    ------------
        Retorna el valor de True si es el dato ingresado es un digito y false si no lo es
    """
    numeroValido = False
    if num.isdigit():
        numeroValido = True
        return numeroValido
    else:
        return numeroValido

        

def perteneceFibonacci(num1):
    """
    Es un procedimiento que nos permite determinar si un numero pertenece a la serie de Fibonacci
    Parametros:
    ------------
        Tiene parametros de entrada, num1 (Es numero que se quiere saber si pertenece a la serie de Fibonacci)
    
    Retorna:
    ------------
        si retorna un valor, esFibonacci (Si el numero pertenece es True, caso contrario False)
    """
    #Inicializa valores, a = 0 y b =1, para iniciar la serie de Fibonacci
    a, b = 0,1
    #Inicializa la variable n = 100, representando el limite de la serie
    n=100
    #Inicializa la variable  esFibonacci=False
    esFibonacci=False
    #Inicio del bucle, serie de Fibonacci
    while a < n:
        #Asigna valores de a = b y b=a+b
        a, b = b, a+b
        #Si a es igual al numero ingresado (num1) entoces
        if a == num1:
            #Se asigana a esFibonacci=True, el numero ingresa si pertenece a la serie
            esFibonacci=True
            #Retorna el valor de esFibonacci
            return esFibonacci
    #Retorna el valor de esFibonacci
    return esFibonacci

##########################################################################################################
#Funcions para el juego 2 Juego de las Sillas
##########################################################################################################
def ingresarNombres(participantes):
    """
    Funcion para guardar los nombres de los participantes en una lista/vector
    de acuerdo al numero de jugadores dado, cada nombre se va adicionando 
    con iteracion de un ciclo for y en la posicion final disponible del vector.

    Parametros:
    ------------
        Recibe como parametro el numero ingresado de participantes del juego (participantes)
    
    Retorna:
    ------------
        Retorna un vector/lista que contiene los nombres de los participantes (listaParticipantes)
    """
    listaJugadores = []
    #Se inicializa una lista Vacia, para posteriormente almacenar los nombres de los jugadores
    #Ciclo repetitivo For para solicitar el ingreso de Nombres de Jugadores 
    for x in range(participantes):
        #El ciclo esta controlado por el numero de jugadores (participantes) Ingresado anteriormente
        print("Ingrese Nombre del Jugador ",x+1, " :")
        nombre = str(input('')) #En cada iteracion se solicita un nombre de Jugador
        #Cada Nombre se va almacenando en la Lista vacia inicializada 
        listaJugadores.append(nombre) #Va almacenando los nombres en la ultima posicion libre 
        
    print("Empieza la Ronda con los siguientes jugadores: \n")
    print(listaJugadores)
    #Se muestra en pantalla la Lista con los participantes de la ronda
    return listaJugadores #retornamos la lista para usarla en la funcion que desarolla el juego

def juegoSillas(participantes,sillas):
    """
   Funcion donde se desarrollara toda la interaccion del juego de las sillas
   se operara con la lista de participantes y se lor ira eliminando hasta que 
   quede un unico participante en la lista, que sera el ganador

   Parametros:
    ------------
        Recibe dos parametros: El numero de participantes (participantes) y el numero de sillas que se usaran(sillas)
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    
    turnos=0 #inicializamos una variable turnos para cada iteracion del juego
    listaJugadores = ingresarNombres(participantes) 
    #llamamos a la funcion ingresarNombres() para que realice su proceso y nos retorne la lista de participantes
    #Inicializamos un ciclo if para cuando el numero de sillas sea mayor que 0
    if (sillas>0):
        for x in range(participantes-1): #Restamos en 1 la longuitud del vector porque la condicion del juego es que debe quedar un ganador
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
            sillas-=1 #Se resta una silla por cada turno 
            time.sleep(2)
            print("Participantes restantes: ",len(listaJugadores), ' ', listaJugadores) 
            print("Sillas restantes: ",sillas) 
            #Se imprime por pantalla el numero de jugadores y sillas restantes
            #Tambien se imprimira el status de la Lista para observar como varia en cada turno

    #Ciclo if que se cumple cuando el valor de las sillas alcanza su valor de 0
    if (sillas == 0):
        print("____________________")
        print("Juego Terminado") #Cuando las sillas llegan a 0 significa que se termino el juego
        #Por tanto se muestra al ganador de la ronda
        print("EL GANADOR ES: ", listaJugadores) #El participante que quede en la lista gana

##########################################################################################################
#Funcions para el juego 3 carta escondida
##########################################################################################################


#JUEGOS
def juego1():
    """
    Es un procedimiento que ejecuta el juego 1: Limbo
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("------------------------\n")
    print("Juego 1: Limbo. Escogido")
    print("------------------------\n")
    #Imprime inicio del juego
    print("------------------------------------------\n")
    print("                  BIENVENIDO              \n")
    print("                JUEGO DEL LIMBO           \n")
    print("------------------------------------------\n")
    #Imprime las reglas del juego
    reglas()
    #Imprime mensaje de ingreso de nombre del jugador y asigna el nombre a nombreJugador
    nombreJugador = input("Por favor ingrese su Nickname: ")
    #Imprime mensaje del primer nivel del limbo
    print("---------------------------------------------\n")
    print("\nNivel 1: Ingrese 2 numeros pares diferentes\n")
    print("---------------------------------------------\n")
    pasoPrimernivel = False
    pasoSegundonivel = False
    pasoTercernivel = False
    while True:
        #Imprime mensaje de ingreso del primer numero y asigna el numero a primerNumero
        primerNumero = input("Por favor ingrese el primer numero: ")
        #Valida que el primer numero sea un numero entero postivo
        if validador(primerNumero) == True:
            #Combierte el dato entrado a Integer(Entero) y lo asigna a primerNumero
         primerNumero=int(primerNumero)
         break
        else:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
            print("--------------------------------------------------------------\n")
    while True:
        #Imprime mensaje de ingreso del segundo numero y asigna el numero a segundoNumero
        segundoNumero = input("Por favor ingrese el segundo numero: ")
        #Valida que el segundo numero sea un numero entero postivo
        if validador(segundoNumero) == True:
            #Combierte el dato entrado a Integer(Entero) y lo asigna a segundoNumero
            segundoNumero=int(segundoNumero)
            break
        else:
            #Imprime mensaje de error en ingreso de datos
            print("--------------------------------------------------------------\n")
            print("                              ERROR                           \n")
            print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
            print("--------------------------------------------------------------\n")
    #Si los dos numeros ingresados son pares y no se repiten entonces
    if (primerNumero % 2 == 0) and (segundoNumero % 2 == 0) and (primerNumero != segundoNumero):
        #Imprime que se paso el nivel uno
        nivelUno()
        #Asigna pase de nivel 1 a verdero
        pasoPrimernivel = True
    else:
        #Imprime el fin del juego
        finDeJuego()
    #Si paso el primer nivel entonces
    if(pasoPrimernivel == True):
        #Imprime mensaje del segundo nivel del limbo
        print("--------------------------------------------------------------\n")
        print("Nivel 2: Ingrese 2 numeros de la serie de fibonacci diferentes\n")
        print("--------------------------------------------------------------\n")
        while True:
            #Imprime mensaje de ingreso del primer numero y asigna el numero a primerNumero
            primerNumero = input("Por favor ingrese el primer numero: ")
            #Valida que el primer numero sea un numero entero postivo
            if validador(primerNumero) == True:
                #Combierte el dato entrado a Integer(Entero) y lo asigna a primerNumero
                primerNumero=int(primerNumero)
                break
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
                print("--------------------------------------------------------------\n")
        while True:
            #Imprime mensaje de ingreso del segundo numero y asigna el numero a segundoNumero
            segundoNumero = input("Por favor ingrese el segundo numero: ")
            #Valida que el segundo numero sea un numero entero postivo
            if validador(segundoNumero) == True:
                #Combierte el dato entrado a Integer(Entero) y lo asigna a segundoNumero
                segundoNumero=int(segundoNumero)
                break
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
                print("--------------------------------------------------------------\n")
    #si los dos nuemeros son diferentes y pertencen a la serie entonces
    if (pasoPrimernivel == True) and (perteneceFibonacci(primerNumero)==True)and (perteneceFibonacci(segundoNumero)==True) and (primerNumero != segundoNumero):
        #Imprime que se paso el nivel dos
        nivelDos()
        #Asigna pase de nivel 2 a verdero
        pasoSegundonivel = True
    elif (pasoPrimernivel == True) and (pasoPrimernivel == False):
        #Imprime el fin del juego
        finDeJuego()

    #si paso el segundo nivel entonces
    if(pasoSegundonivel == True):
        #Imprime mensaje del tercer nivel del limbo
        print("-------------------------------------------------------------------------------\n")
        print("Nivel 3: Ingrese 2 numeros de la serie de fibonacci que sean pares y diferentes\n")
        print("-------------------------------------------------------------------------------\n")
        while True:
            #Imprime mensaje de ingreso del primer numero y asigna el numero a primerNumero
            primerNumero = input("Por favor ingrese el primer numero: ")
            #Valida que el primer numero sea un numero entero postivo
            if validador(primerNumero) == True:
                #Combierte el dato entrado a Integer(Entero) y lo asigna a primerNumero
                primerNumero=int(primerNumero)
                break
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
                print("--------------------------------------------------------------\n")
        while True:
            #Imprime mensaje de ingreso del segundo numero y asigna el numero a segundoNumero
            segundoNumero = input("Por favor ingrese el segundo numero: ")
            #Valida que el segundo numero sea un numero entero postivo
            if validador(segundoNumero) == True:
                #Combierte el dato entrado a Integer(Entero) y lo asigna a segundoNumero
                segundoNumero=int(segundoNumero)
                break
            else:
                #Imprime mensaje de error en ingreso de datos
                print("--------------------------------------------------------------\n")
                print("                              ERROR                           \n")
                print("El dato ingresado no es un numero entero positivo, intente de nuevo.\n")
                print("--------------------------------------------------------------\n")
            #si los dos numeros ingresados son diferentes y pares y pertencen a la serie de fibonacci entonces
        if(pasoSegundonivel == True) and (perteneceFibonacci(primerNumero)==True) and (perteneceFibonacci(segundoNumero)==True) and (primerNumero % 2 == 0) and (segundoNumero % 2 == 0) and (primerNumero != segundoNumero):
            #Imprime que se paso el nivel tres
            nivelTres()
            #Asigna pase de nivel 3 a verdero
            pasoTercernivel = True
            #Imprime mensaje de ganar el juego
            print("------------------------------------------\n")
            print("                  FELICIDADES             \n")
            print("          GANASTE " + nombreJugador +" \n")
            print("             EL JUEGO DEL LIMBO           \n")
            print("------------------------------------------\n")
        else:
            #Imprime el fin del juego
            finDeJuego()
        
    #desarollar Juego 1
def juego2():
    """
    Es un procedimiento que ejecuta el juego 2: Juego de las Sillas
    Parametros:
    ------------
        No tiene parametros de entrada
    
    Retorna:
    ------------
        No retorna ningun valor
    """
    print("------------------------\n")
    print("Juego 2: Juego de Las Sillas. Escogido")
    print("------------------------\n")
    #desarollar Juego 2
    #Declaramos dos variables globales indispensables para desarollar el juego
    #Numero de participantes y numero de sillas
    #Mensaje de Bienvenida y primera indicacion
    print("***BIENVENIDO AL JUEGO DE LAS SILLAS***")
    print("--Para poder jugar se necesitan 2 o mas participantes--")
    """A continuacion se propone un control de ingreso de datos, definido
    por un bucle (While True) y un manejo de excepciones, el ciclo solo se 
    terminara cuando se cumpla la condicion de que el numero
    de participantes ingresados sea un entero y sea mayor que 1
    """
    while True:
        try:
            participantes = int(input("Ingrese el numero de participantes: "))
        except ValueError:
            print("Solo Enteros")
            continue
        if participantes<=1:
            print("Debe haber mas de un jugador")
            continue
        else:
            break       
    #Por regla del juego el numero de sillas corresponde al numero de participantes -1
    sillas = participantes-1
    print("El juego empieza con ",participantes," participantes")
    print("Sillas en juego: " ,sillas)
    #Mensaje de numero de participantes y Sillas
    #ingresarNombres(participantes)
    juegoSillas(participantes, sillas)
    #Llamado a la funcion que desarolla el juego
def juego3():
    print("Juego 3: Busqueda de Parejas. Escogido")    
    #desarollar Juego 3
def salir():
    print("Saliendo")


if __name__ == '__main__':
    #Variables para juego Limbo
    #Inicializa variables paso de nivel correspondiente al nivel, todas en False
    pasoPrimernivel = False
    pasoSegundonivel = False
    pasoTercernivel = False
    nombreJugador = ""
    primerNumero = 0
    segundoNumero = 0
    #Variables para juego de la silla
    participantes = 0 
    sillas = 0
    menuPrincipal()