'''
Objetivo del programa (descripción del problema que resuelve): Realizar el famoso juego de cartas: " Truco" 

Autor/es: Tomas Aguirre, Menchaca Miguel Ángel, Paulo Sosa

Versión:1

Fecha: 15-12-21

Síntesis de Casos (composición de casos para la generalización):
-pedir al usuario que ingrese "SI" para iniciar el juego o "NO" para terminarlo y almacenar respuesta en inicio
-PUNTOSU es igual a cero
-PUNTOSC es igual a cero
-PU es igual a cero
-PC es igual a cero
-de random importar choice
-de random importar shuffle
-variable primero es igual a choice de lista para saber quien inicia
-mientras inicio sea igual a "SI" o "si"
    mientras PU(puntos de usuario en la partida) sea menor igual a 30 y PC((puntos de usuario en la partida) tambien
        si PU es mayor igual a 30 y PC((puntos de usuario en la partida) es menor a 30
            imprimir 'GANASTE LA PARTIDA, FELICITACIONES'
        si PU es menor a 30 y PC((puntos de usuario en la partida) es mayor igual a 30
            imprimir LAMENTABLEMENTE PERDISTE
        -mientras inicio sea igual a "SI" o "si"
            contador es igual a 1
            manos_usuario1, manos_usuario2, manos_usuario3, manos_usuario4,manos_usuario5 y manos_usuario6=0
            manos_cpu1, manos_cpu2, manos_cpu3, manos_cpu4, manos_cpu5 y manos_cpu6=0
            almacenar en variable "mazo" lo que devuelva la funcion mazos
            almacenar en variable "Umsp","Ump","Cmsp" y "Cmp" lo que devuelva la funcion 'cartas' que toma a la variable mazo como parametro
            se sortea quien inicia
            imprimir primero, para determinar quien inicia
            almacenar en UEC y en CEC lo que devuelva la funcion valores con Umsp y Cmsp como parametro
            almacenar en variables manos_usuario1,manos_cpu1,Cmsp,Umsp,Cmp,Ump,PUNTOSU,PUNTOSC,contador,PuntoU,PuntoC lo que devuelva la funcion 'juego' que toma las variables primero,Umsp,Ump,Cmsp,Cmp,UEC,CEC,PUNTOSU,PUNTOSC como parametros
            PU es igual a PU mas PuntoU
            PC es igual a PC mas PuntoC
            si contador!=99

        si manos_usuario1 es igual a 1 y manos_cpu1 es igual a 0
            almacenar en variables manos_usuario2,manos_cpu2,Cmsp,Umsp,Cmp,Ump lo que devuelva la funcion 'MANOUS' que toma las variables Cmsp,Cmp,Umsp,Ump,manos_usuario1,manos_cpu1 como parametros
            
        si manos_usuario2 es igual a 1 y manos_cpu2 es igual a 0
            imprimir 'ganaste la mano'
            si contador es igual a 1
                PU mas igual a 1
            si contador es igual a 2
                PU mas igual a 2
            si contador es igual a 3
                PU mas igual a 3
            si contador es igual a 4
                PU mas igual a 4
                
        si manos_usuario1 es igual a 0 y manos_cpu1 es igual a 1
            almacenar en variables manos_usuario3,manos_cpu3,Cmsp,Umsp,Cmp,Ump lo que devuelva la funcion 'MANOCPU' que toma las variables Cmsp,Cmp,Umsp,Ump,manos_usuario1,manos_cpu1 como parametros

        si manos_usuario3 es igual a 0 y manos_cpu3 es igual a 2
            imprimir 'perdiste la mano'
            si contador es igual a 1
                PU mas igual a 1
            si contador es igual a 2
                PU mas igual a 2
            si contador es igual a 3
                PU mas igual a 3
            si contador es igual a 4
                PU mas igual a 4

        si manos_usuario1 es igual a 1 y manos_cpu1 es igual a 1
            si la partida la inicio el usuario
                almacenar en variables manos_usuario4,manos_cpu4,Cmsp,Umsp,Cmp,Ump lo que devuelva la funcion 'MANOUS' que toma las variables Cmsp,Cmp,Umsp,Ump,manos_usuario1,manos_cpu1 como parametros
            si la partida la inicio el programa
                almacenar en variables manos_usuario4,manos_cpu4,Cmsp,Umsp,Cmp,Ump lo que devuelva la funcion 'MANOCPU' que toma las variables Cmsp,Cmp,Umsp,Ump,manos_usuario1,manos_cpu1 como parametros
        si manos_usuario2 es igual a 1 y manos_cpu2 es igual a 1
            almacenar en variables manos_usuario5,manos_cpu5,Cmsp,Umsp,Cmp,Ump lo que devuelva la funcion 'MANOCPU' que toma las variables Cmsp,Cmp,Umsp,Ump,manos_usuario2,manos_cpu2 como parametros
            si manos_usuario5 es igual a 2 y manos_cpu5 es igual a 2
                imprimir 'ganaste la mano'
                si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
        si manos_usuario3 es igual a 1 y manos_cpu3 es igual a 1
            almacenar en variables manos_usuario5,manos_cpu5,Cmsp,Umsp,Cmp,Ump lo que devuelva la funcion 'MANOUSUARIO' que toma las variables Cmsp,Cmp,Umsp,Ump,manos_usuario2,manos_cpu2 como parametros
            si manos_usuario5 es igual a 2 y manos_cpu5 es igual a 2
                imprimir 'perdiste la mano'
                si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
                    
        si manos_usuario2 es igual a 2 y manos_cpu2 es igual a 1
                imprimir 'ganaste la mano'
                si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
        si manos_usuario4 es igual a 1 y manos_cpu4 es igual a 2
                imprimir 'perdiste la mano'
                si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
                    
        si manos_usuario4 es igual a 2 y manos_cpu4 es igual a 1
                imprimir 'ganaste la mano'
                si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
        si manos_usuario5 es igual a 1 y manos_cpu5 es igual a 2
                imprimir 'perdiste la mano'
               si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
                
        si manos_usuario5 es igual a 2 y manos_cpu5 es igual a 1
                imprimir 'ganaste la mano'
               si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
                    
        si manos_usuario4 es igual a 2 y manos_cpu4 es igual a 2
            si la partida la inicio el usuario
                almacenar en variables Cmsp,Cmp,Usmp,Ump,manos_usuario6,manos_cpu6 lo que devuelva la funcion 'MANOUSUARIO' que toma las variables Cmsp,Cmp,Umsp,Ump,manos_usuario4,manos_cpu4 como parametros
            sino
                almacenar en variables manos_usuario6,manos_cpu6,Cmsp,Umsp,Cmp,Ump lo que devuelva la funcion 'MANOCPU' que toma las variables Cmsp,Cmp,Umsp,Ump,manos_usuario4,manos_cpu4 como parametros

        si manos_usuario6 es igual a 3 y manos_cpu6 es igual a 2
                imprimir 'ganaste la mano'
               si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
        si manos_usuario6 es igual a 2 y manos_cpu5 es igual a 3
                imprimir 'perdiste la mano'
               si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
        si manos_usuario6 es igual a 3 y manos_cpu6 es igual a 3
            si la partida la inicio el usuario
                imprimir 'ganaste la mano'
               si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
            sino
                imprimir 'perdiste la mano'
               si contador es igual a 1
                    PU mas igual a 1
                si contador es igual a 2
                    PU mas igual a 2
                si contador es igual a 3
                    PU mas igual a 3
                si contador es igual a 4
                    PU mas igual a 4
        si el contador es igual a 1000 o 5000
            PC mas igual a 1
        si el contador es igual a 4000
            PU mas igual a 1
        imprimir PU y PC
        TERMINADO es igual a cero
        si PU es mayor igual a 30 y PC es menor a 30
            imprimir ganaste
            TERMINADO=30
        si PC es mayor igual a 30 y PU es menor a 30
            imprimir perdiste
            TERMINADO=30
        si TERMINADO es 0
             pedir al usuario que ingrese "SI" para iniciar el juego o "NO" para terminarlo y almacenar respuesta en inicio
            si inicie yo, primero es igual a inicia el programa
            sino
                primero es iguala a inicio yo
        si TERMINADO es 30
             pedir al usuario que ingrese "SI" para iniciar el juego o "NO" para terminarlo y almacenar respuesta en inicio
            si inicie yo, primero es igual a inicia el programa
            sino
                primero es iguala a inicio yo                
            PU es 0
            PC es 0
            imprimir PU y PC

    
    Datos a solicitar al usuario (sea en el prólogo o sea durante la resolución):
    SI o si, para iniciar el juego
    distinto de SI o si, para terminar el juego

    Recursos (variables y funciones del programa -nombre y propósito)
    Cmsp, lista donde se van almacenando las cartas del programa sin las proridades
    Cmp, lista donde se van almacenando las cartas del programa con las proridades
    Usmp, lista donde se van almacenando las cartas del usuario sin las proridades
    Ump, lista donde se van almacenando las cartas del usuario con las proridades
    inicio, se almacena la respuesta del usuario SI/si desea iniciar el juego o no
    manos_usuario1,2,3,4,5,6, sirve para indicar el camino de la partida 
    manos_cpu1,2,3,4,5,6, sirve para indicar el camino de la partida 
    mazo, se almacena el mazo con el que se va a jugar
    primero, se almacena el resultado de la funcion random choice entre dos elementos de una lista y determina quien inicia el juego
    PU,puntos usuario
    PC,puntos cpu
    UEC,CEC, mazos sin prioridad donde se separan los elementos de una carta( se separa valor y tipo) para usuario y cpu
    contador, utilizado para saber si se canta truco, retruco, vale 4, ninguna de ellas o se abandona la mano
    TERMINADO, variable para controlar el reinicio del juego en caso de q algun jugador llegue a 30 puntos
    
    Funciones propias (necesarias para la descomposición del problema en subproblemas):
    funcion random, especificamente el choice paraa determinar quien inicia el juego
    def mazos, devuelve el mazo del juego
    def cartas, devuelve Cmsp,Cmp,Usmp,Ump
    def juego, funcion para la primer mano de la partida
    def MANOUS, funcion usada luego de que el usuario gane la mano anterior a la que se va a jugar
    def MANOCPU, funcion usada luego de que el programa gane la mano anterior a la que se va a jugar
    def MANOUSUARIO, usada en caso de que la partida tenga dos empates consecutivos en la mano 1 y mano2 y el usuario sea mano  
    valores, funcion usada para obtener los mazos sin prioridad donde se separan los elementos de una carta( se separa valor y tipo) para usuario y cpu
    envidos, usada para todos los envidos en caso de que el usuario sea mano
    envidocpu, usada para todos los envidos en caso de que el programa sea mano
    uenv, usada para obtener la suma de las cartas para el envido

   
'''
# DEFINICIÓN DE FUNCIONES (si se requieren para descomponer la solución del problema)
def mazos():
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    no recibe nada

    Objetivo (descripción de lo que hace o devuelve):
    devolver el mazo de cartas para jugar al truco

    Síntesis de Casos (composición de casos para la generalización):
    -Se escriben las cartas de tipo espada con su valor, tipo y prioridad en comparacion a las demas y se almacenan en la lista Espada
    -Se escriben las cartas de tipo Basto con su valor, tipo y prioridad en comparacion a las demas y se almacenan en la lista Basto
    -Se escriben las cartas de tipo Oro con su valor, tipo y prioridad en comparacion a las demas y se almacenan en la lista Oro
    -Se escriben las cartas de tipo Copa con su valor, tipo y prioridad en comparacion a las demas y se almacenan en la lista Copa
    -Se suman las listas anteriores y se almacenan en una lista llamada mazo
    -devolver mazo
        
    Recursos (variables o funciones internas -nombre y propósito)
        Auxiliares (necesarios para transformaciones intermedias):
        Espada,Basto,Oro,Copa, listas con las cartas separadas por su respectivo tipo
        mazo, se concatenan las listas y se almacenan en una sola
        
        Resultados (si la función devuelve):
        mazo,devuelve el mazo de cartas
        
    '''
    #1 PRÓLOGO  # Establecimiento de valores iniciales para datos auxiliares o que se transformarán en resultados (opcional)
    Espada=[('1','Espada',1),('7','Espada',3),('3','Espada',5),('2','Espada',6),('12','Espada',8),('11','Espada',9),('10','Espada',10),('6','Espada',12),('5','Espada',13),('4','Espada',14)]
    Basto=[('1','Basto',2),('3','Basto',5),('2','Basto',6),('12','Basto',8),('11','Basto',9),('10','Basto',10),('7','Basto',11),('6','Basto',12),('5','Basto',13),('4','Basto',14)]
    Oro=[('7','Oro',4),('3','Oro',5),('2','Oro',6),('1','Oro',7),('12','Oro',8),('11','Oro',9),('10','Oro',10),('6','Oro',12),('5','Oro',13),('4','Oro',14)]
    Copa=[('3','Copa',5),('2','Copa',6),('1','Copa',7),('12','Copa',8),('11','Copa',9),('10','Copa',10),('7','Copa',11),('6','Copa',12),('5','Copa',13),('4','Copa',14)]
    mazo=Espada+Basto+Oro+Copa


    #3 EPÍLOGO # Devolución de valor o valores o muestra de resultados
    return mazo

def cartas(mazo):    
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    mazo, lista mazo con las cartas del truco. Con valor, tipo y prioridad

    Objetivo (descripción de lo que hace o devuelve):
    Obtener una lista con las 3 cartas del usuario (con valor,tipo y prioridad)
    Obtener otra lista con las 3 cartas del usuario (con valor,tipo pero sin prioridad)
    Obtener una lista con las 3 cartas del programa (con valor,tipo y prioridad)
    Obtener otra lista con las 3 cartas del programa (con valor,tipo pero sin prioridad)

    Síntesis de Casos (composición de casos para la generalización):
    -de random importar shuffle
    -inicializar lista Ump,Umsp,Cmp y Cmsp
    -utilizar el shuffle para mezclar la lista mazo
    -carta1 va a ser igual a la carta que se encuentre en la 1er posicion de la lista
    -agregar carta1 a la lista Ump
    -carta2 va a ser igual a la carta que se encuentre en la 2da posicion de la lista
    -agregar carta2 a la lista Ump
    -carta3 va a ser igual a la carta que se encuentre en la 3er posicion de la lista
    -agregar carta3 a la lista Ump
    -carta4 va a ser igual a la carta que se encuentre en la 4ta posicion de la lista
    -agregar carta4 a la lista Cmp
    -carta5 va a ser igual a la carta que se encuentre en la 5ta posicion de la lista
    -agregar carta5 a la lista Cmp
    -carta6 va a ser igual a la carta que se encuentre en la 6ta posicion de la lista
    -agregar carta6 a la lista Cmp
    -para i en el rango de 0 a 3
        A es igual a Ump[i][:-1], para eliminar el ultimo elemento de una posicion, es decir, se elimina la prioridad
        se almacena en Umsp y tenemos las cartas del usuario sin la prioridad
    -para i en el rango de 0 a 3
        A es igual a Cmp[i][:-1], para eliminar el ultimo elemento de una posicion, es decir, se elimina la prioridad
        se almacena en Cmsp y tenemos las cartas del programa sin la prioridad
    -devuelve Umsp,Ump,Cmsp,Cmp

    Recursos (variables o funciones internas -nombre y propósito)
        Auxiliares (necesarios para transformaciones intermedias):
        carta1,carta2,carta3, cartas del usuario
        carta4,carta5,carta6, cartas del programa
        
    Resultados (si la función devuelve):
    Umsp,lista con las 3 cartas del usuario (con valor,tipo pero sin prioridad)
    Ump,lista con las 3 cartas del usuario (con valor,tipo y prioridad)
    Cmsp, lista con las 3 cartas del programa (con valor,tipo pero sin prioridad) 
    Cmp,lista con las 3 cartas del programa (con valor,tipo y prioridad)

    Funciones internas (necesarias para la descomposición del problema en subproblemas):
    random-shuffle: Se utiliza para mezclar las cartas
    '''
    #1 PRÓLOGO
    from random import shuffle
    Ump=[]
    Umsp=[]
    Cmp=[]
    Cmsp=[]

    #2 RESOLUCIÓN
    shuffle(mazo)
    carta1=mazo[0]
    Ump.append(carta1)
    carta2=mazo[1]
    Ump.append(carta2)
    carta3=mazo[2]
    Ump.append(carta3)
    #print('cartas del rival \n')
    carta4=mazo[3]
    #print(carta4)
    carta5=mazo[4]
    #print(carta5)
    carta6=mazo[5]
    #print(carta6)
    Cmp.append(carta4)
    Cmp.append(carta5)
    Cmp.append(carta6)
    
    for i in range(3):
        A=Ump[i][:-1]
        Umsp.append(A)#Mazo sin prioridades
    for i in range(3):
        A=Cmp[i][:-1]
        Cmsp.append(A)#Mazo sin prioridades

    return Umsp,Ump,Cmsp,Cmp

def juego(primero,Umsp,Ump,Cmsp,Cmp,UEC,CEC,PUNTOSU,PUNTOSC):    
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    primero, sirve para determinar quien arranca la mano
    Umsp,lista con las 3 cartas del usuario (con valor,tipo pero sin prioridad)
    Ump,lista con las 3 cartas del usuario (con valor,tipo y prioridad)
    Cmsp, lista con las 3 cartas del programa (con valor,tipo pero sin prioridad) 
    Cmp,lista con las 3 cartas del programa (con valor,tipo y prioridad)
    UEC,CEC, explicado arriba
    PUNTOSU,PUNTOSC, puntos usuario y cpu

    Objetivo (descripción de lo que hace o devuelve):
    determinar si la primer mano la gana el usuario, el programa o hay empate

    Síntesis de Casos (composición de casos para la generalización):
    manos_cpu es igual a 0
    manos_usuario es igual a 0
    contador es igual a 1
    PUNTOU es igual a 0
    PUNTOC es igual a 0
    PuntoU es igual a 0
    PuntoC es igual a 0
    carta1 es Cmp[0][2]
    carta2 es Cmp[1][2]
    carta3 es Cmp[2][2]

    imprimir 'tus cartas son'
    para i en el rango de la longitud de Umsp
        imprimir Cx=X(carta)
    si inicia el usuario
        usamos la funcion envidos
        imprimir: escribir "T" para cantar truco, caso contrario presiona "enter"'
        almacenar en truco la respuesta
        si truco es t o T
            canto truco
            si carta 1 o carta 2 o carta 3 es menor a 11
                el programa acepta
                contador es 2
                PUNTOU es 0
            sino
                el programa no acepta
                contador es 1000
            si contador es 2
                si carta 1 o carta 2 o carta 3 es menor a 5
                    el programa canta retruco
                    almacenar en truco si acepto, si no lo hago o si canto vale4
                    si canto vale 4, contador es 4
        si contador es 1,2,3 o 4
            
            el usuario ingresa C1,C2 o C3 y la respuesta se almacena en first
            si es C1
                imprimir carta 1 sin prioridad
                eliminar carta 1 sin prioridad de Umsp
                Pusuario es igual a prioridad de carta 1
                eliminar carta 1 con prioridad de Ump
            si es C2
                imprimir carta 2 sin prioridad
                eliminar carta 2 sin prioridad de Umsp
                Pusuario es igual a prioridad de carta 2
                eliminar carta 2 con prioridad de Ump
            si es C3
                imprimir carta 3 sin prioridad
                eliminar carta 3 sin prioridad de Umsp
                Pusuario es igual a prioridad de carta 3
                eliminar carta 3 con prioridad de Ump
            CP4 es igual a prioridad de carta4
            CP5 es igual a prioridad de carta5
            CP6 es igual a prioridad de carta6
            si CP4 es menor a Pusuario y CP5 es menor a Pusuario y CP6 es menor a Pusuario:
                si CP4 es igual a CP5 y CP4 es igual a CP6
                    imprimir 'el programa tira carta 4
                    eliminar carta 4 sin prioridad de Cmsp
                    eliminar carta 4 con prioridad de Cmp
                    sumo 1 a manos_cpu
                sino si CP4 es mayor igual a CP5 y CP4 es mayor a CP6
                    imprimir 'el programa tira carta 4
                    eliminar carta 4 sin prioridad de Cmsp
                    eliminar carta 4 con prioridad de Cmp
                    sumo 1 a manos_cpu
                 sino si CP4 es mayor a CP5 y CP4 es mayor igual a CP6
                    imprimir 'el programa tira carta 4
                    eliminar carta 4 sin prioridad de Cmsp
                    eliminar carta 4 con prioridad de Cmp
                    sumo 1 a manos_cpu
                 sino si CP5 es mayor a CP4 y CP5 es mayor igual a CP6
                    imprimir 'el programa tira carta 5
                    eliminar carta 5 sin prioridad de Cmsp
                    eliminar carta 5 con prioridad de Cmp
                    sumo 1 a manos_cpu
                sino si CP5 es mayor igual a CP4 y CP5 es mayor aCP6
                    imprimir 'el programa tira carta 5
                    eliminar carta 5 sin prioridad de Cmsp
                    eliminar carta 5 con prioridad de Cmp
                    sumo 1 a manos_cpu
                sino
                    imprimir 'el programa tira carta 6
                    eliminar carta 6 sin prioridad de Cmsp
                    eliminar carta 6 con prioridad de Cmp
                    sumo 1 a manos_cpu
            si CP4 es menor a Pusuario y CP5 es menor a Pusuario y CP6 es mayor a Pusuario
                si CP4 es mayor igual a CP5
                    imprimir 'el programa tira carta 4
                    eliminar carta 4 sin prioridad de Cmsp
                    eliminar carta 4 con prioridad de Cmp
                    sumo 1 a manos_cpu
                sino
                    imprimir 'el programa tira carta 5
                    eliminar carta 5 sin prioridad de Cmsp
                    eliminar carta 5 con prioridad de Cmp
                    sumo 1 a manos_cpu
            si CP4 es menor a Pusuario y CP5 es mayor a Pusuario y CP6 es mayor a Pusuario
                imprimir 'el programa tira carta 4
                eliminar carta 4 sin prioridad de Cmsp
                eliminar carta 4 con prioridad de Cmp
                sumo 1 a manos_cpu
            si CP4 es mayor a Pusuario y CP5 es mayor a Pusuario y CP6 es mayor a Pusuario
                si CP4 es mayor igual a CP5 y CP4 es mayor igual a CP6
                imprimir 'el programa tira carta 4
                eliminar carta 4 sin prioridad de Cmsp
                eliminar carta 4 con prioridad de Cmp
                sumo 1 a manos_usuario
                sino si CP5 es mayor a CP4 y CP5 es mayor igual a CP6
                    imprimir 'el programa tira carta 5
                    eliminar carta 5 sin prioridad de Cmsp
                    eliminar carta 5 con prioridad de Cmp
                    sumo 1 a manos_usuario
                sino
                    imprimir 'el programa tira carta 6
                    eliminar carta 6 sin prioridad de Cmsp
                    eliminar carta 6 con prioridad de Cmp
                    sumo 1 a manos_usuario
            si CP4 es mayor a Pusuario y CP5 es menor a Pusuario y CP6 es menor a Pusuario
                si CP5 es mayor igual a CP6
                    imprimir 'el programa tira carta 5
                    eliminar carta 5 sin prioridad de Cmsp
                    eliminar carta 5 con prioridad de Cmp
                    sumo 1 a manos_cpu
                sino
                    imprimir 'el programa tira carta 6
                    eliminar carta 6 sin prioridad de Cmsp
                    eliminar carta 6 con prioridad de Cmp
                    sumo 1 a manos_cpu
            si CP4 es mayor a Pusuario y CP5 es mayor a Pusuario y CP6 es menor a Pusuario
                imprimir 'el programa tira carta 6
                eliminar carta 6 sin prioridad de Cmsp
                eliminar carta 6 con prioridad de Cmp
                sumo 1 a manos_cpu
            si CP4 es menor a Pusuario y CP5 es mayor a Pusuario y CP6 es menor a Pusuario
                si CP4 es mayor igual a CP6
                    imprimir 'el programa tira carta 4
                    eliminar carta 4 sin prioridad de Cmsp
                    eliminar carta 4 con prioridad de Cmp
                    sumo 1 a manos_cpu
                sino
                    imprimir 'el programa tira carta 6
                    eliminar carta 6 sin prioridad de Cmsp
                    eliminar carta 6 con prioridad de Cmp
                    sumo 1 a manos_cpu
            si CP4 es mayor a Pusuario y CP5 es menor a Pusuario y CP6 es mayor a Pusuario
                imprimir 'el programa tira carta 5
                eliminar carta 5 sin prioridad de Cmsp
                eliminar carta 5 con prioridad de Cmp
                sumo 1 a manos_cpu
            si CP4 es igual a Pusuario y CP5 es mayor a Pusuario y CP6 es mayor a Pusuario
                imprimir 'el programa tira carta 4
                eliminar carta 4 sin prioridad de Cmsp
                eliminar carta 4 con prioridad de Cmp
                sumo 1 a manos_cpu
                sumo 1 a manos_usuario
            si CP4 es igual a Pusuario y CP5 es igual a Pusuario y CP6 es mayor a Pusuario
                imprimir 'el programa tira carta 4
                eliminar carta 4 sin prioridad de Cmsp
                eliminar carta 4 con prioridad de Cmp
                sumo 1 a manos_cpu
                sumo 1 a manos_usuario
            si CP4 es igual a Pusuario y CP5 es igual a Pusuario y CP6 es igual a Pusuario
                imprimir 'el programa tira carta 4
                eliminar carta 4 sin prioridad de Cmsp
                eliminar carta 4 con prioridad de Cmp
                sumo 1 a manos_cpu
                sumo 1 a manos_usuario
            si CP4 es igual a Pusuario y CP5 es menor a Pusuario y CP6 es menor a Pusuario:
                si CP5 es mayor igual a CP6:
                    imprimir 'el programa tira carta 5
                    eliminar carta 5 sin prioridad de Cmsp
                    eliminar carta 5 con prioridad de Cmp
                    sumo 1 a manos_cpu
                sino
                    imprimir 'el programa tira carta 6
                    eliminar carta 6 sin prioridad de Cmsp
                    eliminar carta 6 con prioridad de Cmp
                    sumo 1 a manos_cpu
            si CP4 es igual a Pusuario y CP5 es igual a Pusuario y CP6 es menor a Pusuario
                imprimir 'el programa tira carta 6
                eliminar carta 6 sin prioridad de Cmsp
                eliminar carta 6 con prioridad de Cmp
                sumo 1 a manos_cpu                
            si CP4 es igual a Pusuario y CP5 es mayor a Pusuario y CP6 es menor a Pusuario
                imprimir 'el programa tira carta 6
                eliminar carta 6 sin prioridad de Cmsp
                eliminar carta 6 con prioridad de Cmp
                sumo 1 a manos_cpu
            si CP4 es igual a Pusuario y CP5 es menor a Pusuario y CP6 es mayor a Pusuario
                imprimir 'el programa tira carta 5
                eliminar carta 5 sin prioridad de Cmsp
                eliminar carta 5 con prioridad de Cmp
                sumo 1 a manos_cpu
            si CP4 es mayor a Pusuario y CP5 es igual a Pusuario y CP6 es mayor a Pusuario
                imprimir 'el programa tira carta 5
                eliminar carta 5 sin prioridad de Cmsp
                eliminar carta 5 con prioridad de Cmp
                sumo 1 a manos_cpu
                sumo 1 a manos_usuario            
            si CP4 es mayor a Pusuario y CP5 es igual a Pusuario y CP6 es igual a Pusuario
                imprimir 'el programa tira carta 5
                eliminar carta 5 sin prioridad de Cmsp
                eliminar carta 5 con prioridad de Cmp
                sumo 1 a manos_cpu
                sumo 1 a manos_usuario
            si CP4 es mayor a Pusuario y CP5 es mayor a Pusuario y CP6 es igual a Pusuario
                imprimir 'el programa tira carta 6
                eliminar carta 6 sin prioridad de Cmsp
                eliminar carta 6 con prioridad de Cmp
                sumo 1 a manos_cpu     
                sumo 1 a manos_usuario    
            si CP4 es mayor a Pusuario y CP5 es menor a Pusuario y CP6 es igual a Pusuario
                imprimir 'el programa tira carta 5
                eliminar carta 5 sin prioridad de Cmsp
                eliminar carta 5 con prioridad de Cmp
                sumo 1 a manos_cpu
            si CP4 es mayor a Pusuario y CP5 es igual a Pusuario y CP6 es menor a Pusuario
                imprimir 'el programa tira carta 6
                eliminar carta 6 sin prioridad de Cmsp
                eliminar carta 6 con prioridad de Cmp
                sumo 1 a manos_cpu    
            si CP4 es menor a Pusuario y CP5 es igual a Pusuario y CP6 es igual a Pusuario
                imprimir 'el programa tira carta 4
                eliminar carta 4 sin prioridad de Cmsp
                eliminar carta 4 con prioridad de Cmp
                sumo 1 a manos_cpu
            si CP4 es igual a Pusuario y CP5 es menor a Pusuario y CP6 es igual a Pusuario
                imprimir 'el programa tira carta 5
                eliminar carta 5 sin prioridad de Cmsp
                eliminar carta 5 con prioridad de Cmp
                sumo 1 a manos_cpu
            si CP4 es menor a Pusuario y CP5 es menor a Pusuario y CP6 es igual a Pusuario
                si CP4 es mayor igual a CP5
                    imprimir 'el programa tira carta 4
                    eliminar carta 4 sin prioridad de Cmsp
                    eliminar carta 4 con prioridad de Cmp
                    sumo 1 a manos_cpu
                sino
                    imprimir 'el programa tira carta 5
                    eliminar carta 5 sin prioridad de Cmsp
                    eliminar carta 5 con prioridad de Cmp
                    sumo 1 a manos_cpu                
            si CP4 es menor a Pusuario y CP5 es mayor a Pusuario y CP6 es igual a Pusuario
                    imprimir 'el programa tira carta 4
                    eliminar carta 4 sin prioridad de Cmsp
                    eliminar carta 4 con prioridad de Cmp
                    sumo 1 a manos_cpu
            si CP4 es menor a Pusuario y CP5 es igual a Pusuario y CP6 es menor a Pusuario
                si CP4 es mayor igual a CP6
                    imprimir 'el programa tira carta 4
                    eliminar carta 4 sin prioridad de Cmsp
                    eliminar carta 4 con prioridad de Cmp
                    sumo 1 a manos_cpu
                sino
                    imprimir 'el programa tira carta 6
                    eliminar carta 6 sin prioridad de Cmsp
                    eliminar carta 6 con prioridad de Cmp
                    sumo 1 a manos_cpu                 
            si CP4 es menor a Pusuario y CP5 es igual a Pusuario y CP6 es mayor a Pusuario
                    imprimir 'el programa tira carta 4
                    eliminar carta 4 sin prioridad de Cmsp
                    eliminar carta 4 con prioridad de Cmp
                    sumo 1 a manos_cpu
    sino
        de random usamos choice para elejir aleatoriamente la carta q va a tirar el programa
        almacenamos en cpu dicha carta
        si cpu es igual la carta en posicion 1 de Csmp
            CPU es igual a prioridad de carta en posicion 1
            eliminar carta en posicion 1 con prioridad de Cmp
        si cpu es igual la carta en posicion 2 de Csmp
            CPU es igual a prioridad de carta en posicion 2
            eliminar carta en posicion 2 con prioridad de Cmp
        si cpu es igual la carta en posicion 3 de Csmp
            CPU es igual a prioridad de carta en posicion 3
            eliminar carta en posicion 3 con prioridad de Cmp
         eliminar elemento identico a cpu de la lista sin prioridad de Cmsp
         funcion envido cpu
         imprimir 'el programa tira cpu'
        el usuario ingresa C1,C2 o C3 y la respuesta se almacena en first
        si es C1
            imprimir carta 1 sin prioridad
            eliminar carta 1 sin prioridad de Umsp
            Pusuario es igual a prioridad de carta 1
            eliminar carta 1 con prioridad de Ump
        si es C2
            imprimir carta 2 sin prioridad
            eliminar carta 2 sin prioridad de Umsp
            Pusuario es igual a prioridad de carta 2
            eliminar carta 2 con prioridad de Ump
        si es C3
            imprimir carta 3 sin prioridad
            eliminar carta 3 sin prioridad de Umsp
            Pusuario es igual a prioridad de carta 3
            eliminar carta 3 con prioridad de Ump
        si Pusuario es menor a CPU:
            ganador 1 es igual a carta
            imprimir 'gano el ganador1'
            sumo 1 a manos_usuario    
        si Pusuario es mayor a CPU
            ganador1=cpu
            sumo 1 a manos_cpu  
            imprimir 'gano el ganador1'
        si Pusuario es igual a CPU
            imprimir 'empate'
            sumo 1 a manos_cpu     
            sumo 1 a manos_usuario    
    devolver manos_usuario,manos_cpu,Cmsp,Umsp,Cmp,Ump,PUNTOSU,PUNTOSC,contador,PuntoU,PuntoC
                
    Recursos (variables o funciones internas -nombre y propósito)
    manos_cpu,sirve para indicar el camino de la partida 
    manos_usuario,sirve para indicar el camino de la partida 
    primero,se almacena el resultado de la funcion random choice entre dos elementos de una lista y determina quien inicia el juego
    Umsp,lista con las 3 cartas del usuario (con valor,tipo pero sin prioridad)
    Ump,lista con las 3 cartas del usuario (con valor,tipo y prioridad)
    Cmsp, lista con las 3 cartas del programa (con valor,tipo pero sin prioridad) 
    Cmp,lista con las 3 cartas del programa (con valor,tipo y prioridad)
    first, se almacena la respuesta del usuario sobre q carta tirara
    Pusuario,prioridad de la carta que tira el usuario
    CP4,CP5,CP6, prioridad de la carta que tira el programa
    cpu, carta aleatoria elegida por el programa
    CPU,prioridad de cpu
        
    Resultados (si la función devuelve):
    manos_usuario,manos_cpu,Cmsp,Umsp,Cmp,Ump
    '''
    manos_cpu=0
    manos_usuario=0
    contador=1
    PUNTOU=0
    PUNTOC=0
    PuntoU=0
    PuntoC=0
    carta1=Cmp[0][2]
    carta2=Cmp[1][2]
    carta3=Cmp[2][2]

    print('Tus cartas son:')
    for i in range(len(Umsp)):
        print(f'C{i+1} es {Umsp[i]}')
    if primero=='TU INICIAS':
        PuntoU,PuntoC,canto=envidos(UEC,CEC,primero)
        
        print('\nEscribir "T" para cantar truco, caso contrario presiona "enter"')
        truco=input('Desea cantar?: ')
        if truco=='T' or truco=='t':
                print('El usuario canto TRUCO')
                if carta1<11 or carta2<11 or carta3<11 :
                    print('El programa acepta')
                    contador=2
                    PUNTOU=0                    
                else:
                    print('El programa no acepta')
                    PUNTOU=1
                    contador=1000

                if contador==2:
                    if carta1<5 or carta2<5 or carta3<5 :
                        print('El programa canta RETRUCO')
                        print('\nEscribir "V" para vale 4, "SI" o "si" para aceptar o "NO" o "no" para abandonar')
                        truco=input('Respuesta: ')
                        if truco=="SI" or truco=="si":
                            print('El usuario acepta')
                            PUNTOC=0
                            contador=3
                        if truco=="NO" or truco=="no":
                            print('El usuario no acepta')
                            PUNTOC=2
                            contador=4000
                        if truco=="V" or truco=="v":
                            contador=4
                            PUNTOC=0
                            print('El usuario canta VALE CUATRO')
                            if carta1<5 or carta2<5 or carta3<5 :
                                print('El programa acepta')
                            else:
                                print('El programa no acepta')
                                PUNTOU=3
                                contador=5000

        if contador==1 or contador==2 or contador==3 or contador==4:        
            print('\nEscribir C (en mayuscula) acompanado de su numero para utilizar una carta\n')    
            first=input('Elije que carta tirar: ')
            if first=='C1':
                print(f'\nEl usuario tira el {Umsp[0]}')
                Umsp.remove(Umsp[0])
                Pusuario=Ump[0][2]
                Ump.remove(Ump[0])
            if first=='C2':
                print(f'\nEl usuario tira el {Umsp[1]}')
                Umsp.remove(Umsp[1])
                Pusuario=Ump[1][2]
                Ump.remove(Ump[1])
            if first=='C3':
                print(f'\nEl usuario tira el {Umsp[2]}')
                Umsp.remove(Umsp[2])
                Pusuario=Ump[2][2]
                Ump.remove(Ump[2])
            CP4=Cmp[0][2]
            CP5=Cmp[1][2]
            CP6=Cmp[2][2]
            if canto=='N' or canto== 'n':
                PuntoU,PuntoC,canto=envidocpu(UEC,CEC,primero)
            if CP4<Pusuario and CP5<Pusuario and CP6<Pusuario:
                if CP4==CP5 and CP4==CP6:
                    print(f'\nEl programa tira el {Cmsp[0]}')
                    Cmsp.remove(Cmsp[0])
                    Cmp.remove(Cmp[0])
                    manos_cpu+=1
                elif CP4>=CP5 and CP4>CP6:
                    print(f'\nEl programa tira el {Cmsp[0]}')
                    Cmsp.remove(Cmsp[0])
                    Cmp.remove(Cmp[0])
                    manos_cpu+=1
                elif CP4>CP5 and CP4>=CP6:
                    print(f'\nEl programa tira el {Cmsp[0]}')
                    Cmsp.remove(Cmsp[0])
                    Cmp.remove(Cmp[0])
                    manos_cpu+=1
                elif CP5>CP4 and CP5>=CP6:
                    print(f'\nEl programa tira el {Cmsp[1]}')
                    Cmsp.remove(Cmsp[1])
                    Cmp.remove(Cmp[1])
                    manos_cpu+=1
                elif CP5>=CP4 and CP5>CP6:
                    print(f'\nEl programa tira el {Cmsp[1]}')
                    Cmsp.remove(Cmsp[1])
                    Cmp.remove(Cmp[1])
                    manos_cpu+=1
                else:
                    print(f'\nEl programa tira el {Cmsp[2]}')
                    Cmsp.remove(Cmsp[2])
                    Cmp.remove(Cmp[2])
                    manos_cpu+=1
            if CP4<Pusuario and CP5<Pusuario and CP6>Pusuario:
                if CP4>=CP5:
                    print(f'\nEl programa tira el {Cmsp[0]}')
                    Cmsp.remove(Cmsp[0])
                    Cmp.remove(Cmp[0])
                    manos_cpu+=1
                else:
                    print(f'\nEl programa tira el {Cmsp[1]}')
                    Cmsp.remove(Cmsp[1])
                    Cmp.remove(Cmp[1])
                    manos_cpu+=1
            if CP4<Pusuario and CP5>Pusuario and CP6>Pusuario:
                print(f'\nEl programa tira el {Cmsp[0]}')
                Cmsp.remove(Cmsp[0])
                Cmp.remove(Cmp[0])
                manos_cpu+=1
            if CP4>Pusuario and CP5>Pusuario and CP6>Pusuario:
                if CP4>=CP5 and CP4>=CP6:
                    print(f'\nEl programa tira el {Cmsp[0]}')
                    Cmsp.remove(Cmsp[0])
                    Cmp.remove(Cmp[0])
                    manos_usuario+=1
                elif CP5>CP4 and CP5>=CP6:
                    print(f'\nEl programa tira el {Cmsp[1]}')
                    Cmsp.remove(Cmsp[1])
                    Cmp.remove(Cmp[1])
                    manos_usuario+=1
                else:
                    print(f'\nEl programa tira el {Cmsp[2]}')
                    Cmsp.remove(Cmsp[2])
                    Cmp.remove(Cmp[2])
                    manos_usuario+=1
            if CP4>Pusuario and CP5<Pusuario and CP6<Pusuario:
                if CP5>=CP6:
                    print(f'\nEl programa tira el {Cmsp[1]}')
                    Cmsp.remove(Cmsp[1])
                    Cmp.remove(Cmp[1])
                    manos_cpu+=1
                else:
                    print(f'\nEl programa tira el {Cmsp[2]}')
                    Cmsp.remove(Cmsp[2])
                    Cmp.remove(Cmp[2])
                    manos_cpu+=1    
            if CP4>Pusuario and CP5>Pusuario and CP6<Pusuario:
                print(f'\nEl programa tira el {Cmsp[2]}')
                Cmsp.remove(Cmsp[2])
                Cmp.remove(Cmp[2])
                manos_cpu+=1
            if CP4<Pusuario and CP5>Pusuario and CP6<Pusuario:
                if CP4>=CP6:
                    print(f'\nEl programa tira el {Cmsp[0]}')
                    Cmsp.remove(Cmsp[0])
                    Cmp.remove(Cmp[0])
                    manos_cpu+=1
                else:
                    print(f'\nEl programa tira el {Cmsp[2]}')
                    Cmsp.remove(Cmsp[2])
                    Cmp.remove(Cmp[2])
                    manos_cpu+=1
            if CP4>Pusuario and CP5<Pusuario and CP6>Pusuario:
                print(f'\nEl programa tira el {Cmsp[1]}')
                Cmsp.remove(Cmsp[1])
                Cmp.remove(Cmp[1])
                manos_cpu+=1
            if CP4==Pusuario and CP5>Pusuario and CP6>Pusuario:
                print(f'\nEl programa tira el {Cmsp[0]}')
                Cmsp.remove(Cmsp[0])
                Cmp.remove(Cmp[0])
                manos_cpu+=1
                manos_usuario+=1
            if CP4==Pusuario and CP5==Pusuario and CP6>Pusuario:
                print(f'\nEl programa tira el {Cmsp[0]}')
                Cmsp.remove(Cmsp[0])
                Cmp.remove(Cmp[0])
                manos_cpu+=1
                manos_usuario+=1
            if CP4==Pusuario and CP5==Pusuario and CP6==Pusuario:
                print(f'\nEl programa tira el {Cmsp[0]}')
                Cmsp.remove(Cmsp[0])
                Cmp.remove(Cmp[0])
                manos_cpu+=1
                manos_usuario+=1
            if CP4==Pusuario and CP5<Pusuario and CP6<Pusuario:
                if CP5>=CP6:
                    print(f'\nEl programa tira el {Cmsp[1]}')
                    Cmsp.remove(Cmsp[1])
                    Cmp.remove(Cmp[1])
                    manos_cpu+=1
                else:
                    print(f'\nEl programa tira el {Cmsp[2]}')
                    Cmsp.remove(Cmsp[2])
                    Cmp.remove(Cmp[2])
                    manos_cpu+=1
            if CP4==Pusuario and CP5==Pusuario and CP6<Pusuario:
                print(f'\nEl programa tira el {Cmsp[2]}')
                Cmsp.remove(Cmsp[2])
                Cmp.remove(Cmp[2])
                manos_cpu+=1            
            if CP4==Pusuario and CP5>Pusuario and CP6<Pusuario:
                print(f'\nEl programa tira el {Cmsp[2]}')
                Cmsp.remove(Cmsp[2])
                Cmp.remove(Cmp[2])
                manos_cpu+=1
            if CP4==Pusuario and CP5<Pusuario and CP6>Pusuario:
                print(f'\nEl programa tira el {Cmsp[1]}')
                Cmsp.remove(Cmsp[1])
                Cmp.remove(Cmp[1])
                manos_cpu+=1
            if CP4>Pusuario and CP5==Pusuario and CP6>Pusuario:
                print(f'\nEl programa tira el {Cmsp[1]}')
                Cmsp.remove(Cmsp[1])
                Cmp.remove(Cmp[1])
                manos_cpu+=1
                manos_usuario+=1
            if CP4>Pusuario and CP5==Pusuario and CP6==Pusuario:
                print(f'\nEl programa tira el {Cmsp[1]}')
                Cmsp.remove(Cmsp[1])
                Cmp.remove(Cmp[1])
                manos_cpu+=1
                manos_usuario+=1
            if CP4>Pusuario and CP5>Pusuario and CP6==Pusuario:
                print(f'\nEl programa tira el {Cmsp[2]}')
                Cmsp.remove(Cmsp[2])
                Cmp.remove(Cmp[2])
                manos_cpu+=1
                manos_usuario+=1
            if CP4>Pusuario and CP5<Pusuario and CP6==Pusuario:
                print(f'\nEl programa tira el {Cmsp[1]}')
                Cmsp.remove(Cmsp[1])
                Cmp.remove(Cmp[1])
                manos_cpu+=1
            if CP4>Pusuario and CP5==Pusuario and CP6<Pusuario:
                print(f'\nEl programa tira el {Cmsp[2]}')
                Cmsp.remove(Cmsp[2])
                Cmp.remove(Cmp[2])
                manos_cpu+=1
            if CP4<Pusuario and CP5==Pusuario and CP6==Pusuario:
                print(f'\nEl programa tira el {Cmsp[0]}')
                Cmsp.remove(Cmsp[0])
                Cmp.remove(Cmp[0])
                manos_cpu+=1
            if CP4==Pusuario and CP5<Pusuario and CP6==Pusuario:
                print(f'\nEl programa tira el {Cmsp[1]}')
                Cmsp.remove(Cmsp[1])
                Cmp.remove(Cmp[1])
                manos_cpu+=1
            if CP4<Pusuario and CP5<Pusuario and CP6==Pusuario:
                if CP4>=CP5:
                    print(f'\nEl programa tira el {Cmsp[0]}')
                    Cmsp.remove(Cmsp[0])
                    Cmp.remove(Cmp[0])
                    manos_cpu+=1
                else:
                    print(f'\nEl programa tira el {Cmsp[1]}')
                    Cmsp.remove(Cmsp[1])
                    Cmp.remove(Cmp[1])
                    manos_cpu+=1
            if CP4<Pusuario and CP5>Pusuario and CP6==Pusuario:
                print(f'\nEl programa tira el {Cmsp[0]}')
                Cmsp.remove(Cmsp[0])
                Cmp.remove(Cmp[0])
                manos_cpu+=1
            if CP4<Pusuario and CP5==Pusuario and CP6<Pusuario:
                if CP4>=CP6:
                    print(f'\nEl programa tira el {Cmsp[0]}')
                    Cmsp.remove(Cmsp[0])
                    Cmp.remove(Cmp[0])
                    manos_cpu+=1
                else:
                    print(f'\nEl programa tira el {Cmsp[2]}')
                    Cmsp.remove(Cmsp[2])
                    Cmp.remove(Cmp[2])
                    manos_cpu+=1
            if CP4<Pusuario and CP5==Pusuario and CP6>Pusuario:
                print(f'\nEl programa tira el {Cmsp[0]}')
                Cmsp.remove(Cmsp[0])
                Cmp.remove(Cmp[0])
                manos_cpu+=1
        else:
            print('MANO TERMNADA')
            contador=99
    else:
        cpu=choice(Cmsp)
        if cpu==Cmsp[0]:
            CPU=Cmp[0][2]
            Cmp.remove(Cmp[0])
        if cpu==Cmsp[1]:
            CPU=Cmp[1][2]
            Cmp.remove(Cmp[1])
        if cpu==Cmsp[2]:
            CPU=Cmp[2][2]
            Cmp.remove(Cmp[2])
        Cmsp.remove(cpu)
        PuntoU,PuntoC,CANTO=envidocpu(UEC,CEC,primero)
        print(f'\nEl programa tira el {cpu}')
        if CANTO=='NOPA':
            PuntoU,PuntoC,canto=envidos(UEC,CEC,primero)
        first=input('Elije que carta tirar: ')
        if first=='C1':
            print(f'\nEl usuario tira el {Umsp[0]}')
            carta=Umsp[0]
            Umsp.remove(Umsp[0])
            Pusuario=Ump[0][2]
            Ump.remove(Ump[0])
        if first=='C2':
            print(f'\nEl usuario tira el {Umsp[1]}')
            carta=Umsp[1]
            Umsp.remove(Umsp[1])
            Pusuario=Ump[1][2]
            Ump.remove(Ump[1])
        if first=='C3':
            print(f'\nEl usuario tira el {Umsp[2]}')
            carta=Umsp[2]
            Umsp.remove(Umsp[2])
            Pusuario=Ump[2][2]
            Ump.remove(Ump[2])
        if Pusuario<CPU:
            ganador1 =carta
            print(f'\nGano el {ganador1}')
            manos_usuario+=1
        if CPU<Pusuario:
            ganador1=cpu
            print(f'\nGano el {ganador1}')
            manos_cpu+=1            
        if CPU==Pusuario:
            print('\nEmpate en la mano')
            manos_cpu+=1            
            manos_usuario+=1            
    return manos_usuario,manos_cpu,Cmsp,Umsp,Cmp,Ump,PUNTOSU,PUNTOSC,contador,PuntoU,PuntoC

def MANOUS(Cmsp,Cmp,Umsp,Ump,manos_usuario1,manos_cpu1):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    Cmsp, lista donde se van almacenando las cartas del programa sin las proridades
    Cmp, lista donde se van almacenando las cartas del programa con las proridades
    Usmp, lista donde se van almacenando las cartas del usuario sin las proridades
    Ump, lista donde se van almacenando las cartas del usuario con las proridades
    manos_usuario1 sirve para indicar el camino de la partida 
    manos_cpu1, sirve para indicar el camino de la partida

    Objetivo (descripción de lo que hace o devuelve):
    funcion usada luego de que el usuario gane la mano anterior a la que se va a jugar

    Síntesis de Casos (composición de casos para la generalización):
    imprimir 'tus cartas son'
    para i en el rango de la longitud de Umsp
        imprimir Cx=X(carta)
    el usuario ingresa C1,C2 o C3 y la respuesta se almacena en first
    si es C1
        imprimir carta 1 sin prioridad
        eliminar carta 1 sin prioridad de Umsp
        Pusuario es igual a prioridad de carta 1
        eliminar carta 1 con prioridad de Ump
    si es C2
        imprimir carta 2 sin prioridad
        eliminar carta 2 sin prioridad de Umsp
        Pusuario es igual a prioridad de carta 2
        eliminar carta 2 con prioridad de Ump
    CP4 es igual a prioridad de carta4
    CP5 es igual a prioridad de carta5

    si CP4 es mayor a Pusuario y CP5 es mayor a Pusuario
        si CP4 mayor igual a CP5
            imprimir 'el programa tira carta 4
            eliminar carta 4 sin prioridad de Cmsp
            eliminar carta 4 con prioridad de Cmp
            sumo 1 a manos_usuario1
        sino
            imprimir 'el programa tira carta 5
            eliminar carta 5 sin prioridad de Cmsp
            eliminar carta 5 con prioridad de Cmp
            sumo 1 a manos_usuario1
    si CP4 es menor a Pusuario y CP5 es mayor a Pusuario
        imprimir 'el programa tira carta 4
        eliminar carta 4 sin prioridad de Cmsp
        eliminar carta 4 con prioridad de Cmp
        sumo 1 a manos_cpu1
    si CP4 es mayor a Pusuario y CP5 es menor a Pusuario
        imprimir 'el programa tira carta 5
        eliminar carta 5 sin prioridad de Cmsp
        eliminar carta 5 con prioridad de Cmp
        sumo 1 a manos_cpu1
    si CP4 es menor a Pusuario y CP5 es menor a Pusuario:
        si CP4 es mayor igual a CP5:
            imprimir 'el programa tira carta 4
            eliminar carta 4 sin prioridad de Cmsp
            eliminar carta 4 con prioridad de Cmp
            sumo 1 a manos_cpu1
        sino
            imprimir 'el programa tira carta 5
            eliminar carta 5 sin prioridad de Cmsp
            eliminar carta 5 con prioridad de Cmp
            sumo 1 a manos_cpu1
    si CP4 es igual a Pusuario y CP5 es mayor a Pusuario
        imprimir 'el programa tira carta 4
        eliminar carta 4 sin prioridad de Cmsp
        eliminar carta 4 con prioridad de Cmp
        sumo 1 a manos_cpu1        
        sumo 1 a manos_usuario1        
    si CP4 es igual a Pusuario y CP5 es menor a Pusuario
        imprimir 'el programa tira carta 5
        eliminar carta 5 sin prioridad de Cmsp
        eliminar carta 5 con prioridad de Cmp
        sumo 1 a manos_cpu1
    si CP4 es igual a Pusuario y CP5 es igual a Pusuario
        imprimir 'el programa tira carta 4
        eliminar carta 4 sin prioridad de Cmsp
        eliminar carta 4 con prioridad de Cmp
        sumo 1 a manos_cpu1        
        sumo 1 a manos_usuario1 
    si CP4 es mayor a Pusuario y CP5 es igual a Pusuario
        imprimir 'el programa tira carta 5
        eliminar carta 5 sin prioridad de Cmsp
        eliminar carta 5 con prioridad de Cmp
        sumo 1 a manos_cpu1        
        sumo 1 a manos_usuario1 
    si CP4 es menor a Pusuario y CP5 es igual a Pusuario
        imprimir 'el programa tira carta 4
        eliminar carta 4 sin prioridad de Cmsp
        eliminar carta 4 con prioridad de Cmp
        sumo 1 a manos_cpu1
    devolver manos_usuario1,manos_cpu1,Cmsp,Umsp,Cmp,Ump

    Recursos (variables o funciones internas -nombre y propósito)
    manos_cpu1,sirve para indicar el camino de la partida 
    manos_usuario1,sirve para indicar el camino de la partida 
    Umsp,lista con las 3 cartas del usuario (con valor,tipo pero sin prioridad)
    Ump,lista con las 3 cartas del usuario (con valor,tipo y prioridad)
    Cmsp, lista con las 3 cartas del programa (con valor,tipo pero sin prioridad) 
    Cmp,lista con las 3 cartas del programa (con valor,tipo y prioridad)
    first, se almacena la respuesta del usuario sobre q carta tirara
    Pusuario,prioridad de la carta que tira el usuario
    CP4,CP5, prioridad de la carta que tira el programa

        
    Resultados (si la función devuelve):
    manos_usuario1,manos_cpu1,Cmsp,Umsp,Cmp,Ump
    '''
    print('\nTus cartas son:')
    for i in range(len(Umsp)):
        print(f'C{i+1} es {Umsp[i]}')
    first=input('Elije que carta tirar: ')
    if first=='C1':
        print(f'\nEl usuario tira el {Umsp[0]}')
        Umsp.remove(Umsp[0])
        Pusuario=Ump[0][2]
        Ump.remove(Ump[0])
    if first=='C2':
        print(f'\nEl usuario tira el {Umsp[1]}')
        Umsp.remove(Umsp[1])
        Pusuario=Ump[1][2]
        Ump.remove(Ump[1])
    CP4=Cmp[0][2]
    CP5=Cmp[1][2]
    if CP4>Pusuario and CP5>Pusuario:
        if CP4>=CP5:
            print(f'\nEl programa tira el {Cmsp[0]}')
            Cmsp.remove(Cmsp[0])
            Cmp.remove(Cmp[0])
            manos_usuario1+=1
        else:
            print(f'\nEl programa tira el {Cmsp[1]}')
            Cmsp.remove(Cmsp[1])
            Cmp.remove(Cmp[1])
            manos_usuario1+=1
    if CP4<Pusuario and CP5>Pusuario:
        print(f'\nEl programa tira el {Cmsp[0]}')
        Cmsp.remove(Cmsp[0])
        Cmp.remove(Cmp[0])
        manos_cpu1+=1
    if CP4>Pusuario and CP5<Pusuario:
        print(f'\nEl programa tira el {Cmsp[1]}')
        Cmsp.remove(Cmsp[1])
        Cmp.remove(Cmp[1])
        manos_cpu1+=1
    if CP4<Pusuario and CP5<Pusuario:
        if CP4>=CP5:
            print(f'\nEl programa tira el {Cmsp[0]}')
            Cmsp.remove(Cmsp[0])
            Cmp.remove(Cmp[0])
            manos_cpu1+=1
        else:
            print(f'\nEl programa tira el {Cmsp[1]}')
            Cmsp.remove(Cmsp[1])
            Cmp.remove(Cmp[1])
            manos_cpu1+=1
    if CP4==Pusuario and CP5>Pusuario:
        print(f'\nEl programa tira el {Cmsp[0]}')
        Cmsp.remove(Cmsp[0])
        Cmp.remove(Cmp[0])
        manos_cpu1+=1
        manos_usuario1+=1
    if CP4==Pusuario and CP5<Pusuario:
        print(f'\nEl programa tira el {Cmsp[1]}')
        Cmsp.remove(Cmsp[1])
        Cmp.remove(Cmp[1])
        manos_cpu1+=1
    if CP4==Pusuario and CP5==Pusuario:
        print(f'\nEl programa tira el {Cmsp[0]}')
        Cmsp.remove(Cmsp[0])
        Cmp.remove(Cmp[0])
        manos_cpu1+=1
        manos_usuario1+=1
    if CP5==Pusuario and CP4>Pusuario:
        print(f'\nEl programa tira el {Cmsp[1]}')
        Cmsp.remove(Cmsp[1])
        Cmp.remove(Cmp[1])
        manos_cpu1+=1
        manos_usuario1+=1
    if CP5==Pusuario and CP4<Pusuario:
        print(f'\nEl programa tira el {Cmsp[0]}')
        Cmsp.remove(Cmsp[0])
        Cmp.remove(Cmp[0])
        manos_cpu1+=1
    return manos_usuario1,manos_cpu1,Cmsp,Umsp,Cmp,Ump

def MANOCPU (Cmsp,Cmp,Umsp,Ump,manos_usuario,manos_cpu):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    Cmsp, lista donde se van almacenando las cartas del programa sin las proridades
    Cmp, lista donde se van almacenando las cartas del programa con las proridades
    Usmp, lista donde se van almacenando las cartas del usuario sin las proridades
    Ump, lista donde se van almacenando las cartas del usuario con las proridades
    manos_usuario, sirve para indicar el camino de la partida 
    manos_cpu, sirve para indicar el camino de la partida

    Objetivo (descripción de lo que hace o devuelve):
    funcion usada luego de que el programa gane la mano anterior a la que se va a jugar

    Síntesis de Casos (composición de casos para la generalización):
    de random usamos choice para elejir aleatoriamente la carta q va a tirar el programa
    almacenamos en cpu dicha carta
    si la longitud de Cmsp es igual a 2
        si cpu es igual la carta en posicion 1 de Csmp
            CPU es igual a prioridad de carta en posicion 1
            eliminar carta en posicion 1 con prioridad de Cmp
        si cpu es igual la carta en posicion 2 de Csmp
            CPU es igual a prioridad de carta en posicion 2
            eliminar carta en posicion 2 con prioridad de Cmp
    si la longitud de Cmsp es igual a 1
        si cpu es igual la carta en posicion 1 de Csmp
            CPU es igual a prioridad de carta en posicion 1
            eliminar carta en posicion 1 con prioridad de Cmp
    eliminar elemento identico a cpu de la lista sin prioridad de Cmsp
    imprimir 'el programa tira 'cpu'
    imprimir 'tus cartas son'
    para i en el rango de la longitud de Umsp
        imprimir Cx=X(carta)
    el usuario ingresa C1,C2 y la respuesta se almacena en first
    si es C1
        imprimir carta 1 sin prioridad
        eliminar carta 1 sin prioridad de Umsp
        Pusuario es igual a prioridad de carta 1
        eliminar carta 1 con prioridad de Ump
    si es C2
        imprimir carta 2 sin prioridad
        eliminar carta 2 sin prioridad de Umsp
        Pusuario es igual a prioridad de carta 2
        eliminar carta 2 con prioridad de Ump
    si Pusuario es menor a CPU:
        ganador 1 es igual a carta
        imprimir 'gano el ganador1'
        sumo 1 a manos_usuario    
    si Pusuario es mayor a CPU
        ganador1=cpu
        sumo 1 a manos_cpu  
        imprimir 'gano el ganador1'
    si Pusuario es igual a CPU
        imprimir 'empate'
        sumo 1 a manos_cpu     
        sumo 1 a manos_usuario    
    devolver manos_usuario,manos_cpu,Cmsp,Umsp,Cmp,Ump

    Recursos (variables o funciones internas -nombre y propósito)
    cpu, carta aleatoria elegida por el programa
    CPU,prioridad de cpu
    Cmsp, lista donde se van almacenando las cartas del programa sin las proridades
    Cmp, lista donde se van almacenando las cartas del programa con las proridades
    Usmp, lista donde se van almacenando las cartas del usuario sin las proridades
    Ump, lista donde se van almacenando las cartas del usuario con las proridades
    inicio, se almacena la respuesta del usuario SI/si desea iniciar el juego o no
    manos_usuario sirve para indicar el camino de la partida 
    manos_cpu sirve para indicar el camino de la partida
    first, se almacena la respuesta del usuario sobre q carta tirara

        
    Resultados (si la función devuelve):
    manos_usuario,manos_cpu,Cmsp,Umsp,Cmp,Ump
    '''
    cpu=choice(Cmsp)
    if len(Cmsp)==2:
        if cpu==Cmsp[0]:
            CPU=Cmp[0][2]
            Cmp.remove(Cmp[0])
        if cpu==Cmsp[1]:
            CPU=Cmp[1][2]
            Cmp.remove(Cmp[1])
    if len(Cmsp)==1:
        if cpu==Cmsp[0]:
            CPU=Cmp[0][2]
            Cmp.remove(Cmp[0])
    Cmsp.remove(cpu)
    print(f'\nEl programa tira el {cpu}')
    print('\nTus cartas son:')
    for i in range(len(Umsp)):
        print(f'C{i+1} es {Umsp[i]}')
    first=input('Elije que carta tirar: ')
    if first=='C1':
        print(f'\nEl usuario tira el {Umsp[0]}')
        carta=Umsp[0]
        Umsp.remove(Umsp[0])
        Pusuario=Ump[0][2]
        Ump.remove(Ump[0])
    if first=='C2':
        print(f'\nEl usuario tira el {Umsp[1]}')
        carta=Umsp[1]
        Umsp.remove(Umsp[1])
        Pusuario=Ump[1][2]
        Ump.remove(Ump[1])
    if Pusuario<CPU:
        ganador1 =carta
        print(f'\nGano el {ganador1}')
        manos_usuario+=1
    if CPU<Pusuario:
        ganador1=cpu
        print(f'\nGano el {ganador1}')
        manos_cpu+=1            
    if CPU==Pusuario:
        print('\nEMPATE')
        manos_cpu+=1 
        manos_usuario+=1    
    return manos_usuario,manos_cpu,Cmsp,Umsp,Cmp,Ump
    
def MANOUSUARIO(Cmsp,Cmp,Umsp,Ump,manos_usuario,manos_cpu):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    Cmsp, lista donde se van almacenando las cartas del programa sin las proridades
    Cmp, lista donde se van almacenando las cartas del programa con las proridades
    Usmp, lista donde se van almacenando las cartas del usuario sin las proridades
    Ump, lista donde se van almacenando las cartas del usuario con las proridades
    manos_usuario, sirve para indicar el camino de la partida 
    manos_cpu, sirve para indicar el camino de la partida

    Objetivo (descripción de lo que hace o devuelve):
    usada en caso de que la partida tenga dos empates consecutivos en la mano 1 y mano2 y el usuario sea mano

    Síntesis de Casos (composición de casos para la generalización):
    imprimit 'tus cartas son'
    para i en el rango de la longitud de Umsp
        imprimir Cx=X(carta)
    si inicia el usuario
        el usuario ingresa C1,C2 o C3 y la respuesta se almacena en first
        si es C1
            imprimir carta 1 sin prioridad
            eliminar carta 1 sin prioridad de Umsp
            Pusuario es igual a prioridad de carta 1
            eliminar carta 1 con prioridad de Ump
    CP4 es igual a prioridad de carta4
    si CP4 es mayor a Pusuario
        imprimir 'el programa tira carta 4
        eliminar carta 4 sin prioridad de Cmsp
        eliminar carta 4 con prioridad de Cmp
        sumo 1 a manos_usuario
    si CP4 es menor a Pusuario
        imprimir 'el programa tira carta 4
        eliminar carta 4 sin prioridad de Cmsp
        eliminar carta 4 con prioridad de Cmp
        sumo 1 a manos_cpu
    si CP4 es igual a Pusuario
        imprimir 'el programa tira carta 4
        eliminar carta 4 sin prioridad de Cmsp
        eliminar carta 4 con prioridad de Cmp
        sumo 1 a manos_usuario
        
    Recursos (variables o funciones internas -nombre y propósito)
    first, se almacena la respuesta del usuario sobre q carta tirara
    Umsp,lista con las 3 cartas del usuario (con valor,tipo pero sin prioridad)
    Ump,lista con las 3 cartas del usuario (con valor,tipo y prioridad)
    Cmsp, lista con las 3 cartas del programa (con valor,tipo pero sin prioridad) 
    Cmp,lista con las 3 cartas del programa (con valor,tipo y prioridad)
     Pusuario,prioridad de la carta que tira el usuario
    CP4, prioridad de la carta que tira el programa
    manos_cpu,sirve para indicar el camino de la partida 
    manos_usuario,sirve para indicar el camino de la partida 

    Resultados (si la función devuelve):
    Cmsp,Cmp,Umsp,Ump,manos_usuario,manos_cpu
    '''
    print('\nTus cartas son:')
    for i in range(len(Umsp)):
        print(f'C{i+1} es {Umsp[i]}')
    first=input('Elije que carta tirar: ')
    if first=='C1':
        print(f'\nEl usuario tira el {Umsp[0]}')
        Umsp.remove(Umsp[0])
        Pusuario=Ump[0][2]
        Ump.remove(Ump[0])
    CP4=Cmp[0][2]
    if CP4>Pusuario:
        print(f'\nEl programa tira el {Cmsp[0]}')
        Cmsp.remove(Cmsp[0])
        Cmp.remove(Cmp[0])
        manos_usuario+=1
    if CP4<Pusuario:
        print(f'\nEl programa tira el {Cmsp[0]}')
        Cmsp.remove(Cmsp[0])
        Cmp.remove(Cmp[0])
        manos_cpu+=1
    if CP4==Pusuario:
        print(f'\nEl programa tira el {Cmsp[0]}')
        Cmsp.remove(Cmsp[0])
        Cmp.remove(Cmp[0])
        manos_usuario+=1
    return (Cmsp,Cmp,Umsp,Ump,manos_usuario,manos_cpu)

def valores(Umsp,Cmsp):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    Umsp, mazo del usuario sin prioridad

    Objetivo (descripción de lo que hace o devuelve):
    establecer los valores de las cartas para la suma de ellas en el envido y almacenarlas en dos listas, una para el usuario y otra para el programa
        
    Síntesis de Casos (composición de casos para la generalización):
    inicializar UEC y CEC
    agregar a UEC los elementos de Umsp pero se separa el valor de la carta con su tipo
    agregar a CEC los elementos de Cmsp pero se separa el valor de la carta con su tipo
    para i en el rango de la longitud de UEC
        si UEC en la posicion i es 10,11,12
            UEC en la posicion i es 0
        si CEC en la posicion i es 10,11,12
            CEC en la posicion i es 0
    devolver UEC y CEC

    Recursos (variables o funciones internas -nombre y propósito)
    UEC, se almacenan  los elementos de Umsp pero se separa el valor de la carta con su tipo
    CEC, se almacenan  los elementos de Cmsp pero se separa el valor de la carta con su tipo

    Resultados (si la función devuelve):
    UEC,CEC
        
    '''
    UEC=[]
    CEC=[]
    UEC.append(Umsp[0][0])
    UEC.append(Umsp[0][1])
    UEC.append(Umsp[1][0])
    UEC.append(Umsp[1][1])
    UEC.append(Umsp[2][0])
    UEC.append(Umsp[2][1])
    CEC.append(Cmsp[0][0])
    CEC.append(Cmsp[0][1])
    CEC.append(Cmsp[1][0])
    CEC.append(Cmsp[1][1])
    CEC.append(Cmsp[2][0])
    CEC.append(Cmsp[2][1])

    for i in range (len(UEC)):
        if UEC[i]=='10' or UEC[i]=='11' or UEC[i]=='12':
            UEC[i]='0'
        if CEC[i]=='10' or CEC[i]=='11' or CEC[i]=='12':
            CEC[i]='0'
   
    #UEC = valores para envido del usuario
    #CEC = valores para envido del programa
    return UEC,CEC

def envidos(UEC,CEC,primero):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    UEC,CEC,primero
    
    Objetivo (descripción de lo que hace o devuelve):
    para el envido si inicia el usuario
    
    Síntesis de Casos (composición de casos para la generalización):
    se crea una herramienta para la toma de decisiones
    PUNTOSU es 0
    PUNTOSC es 0
    sumaus=uenv(UEC)
    sumacpu=uenv(CEC)
    puedo cantar enviso,real,falta o no cantar nada
    almacenar respuesta en canto
    si canto envido
        el programa acepta
        el programa no acepta
        si el programa canta envido
            puedo cantar real,falta, aceptar el envido o rechazar la propuesta
            si canto real
                el programa acepta
                el programa no acepta
                si el programa canta falta
                    acepto
                    no acepto
        si el programa canta real
            puedo cantar falta, aceptar el envido o rechazar la propuesta
        si el programa canta falta
            puedo aceptar o no
    si canto real
        el programa acepta
        el programa no acepta
        si el programa canta falta
            acepto
            no acepto
    si canto falta
        el programa acepta o no
    devuelve PUNTOSU,PUNTOSC,canto
    
    Recursos (variables o funciones internas -nombre y propósito)
    decision,2,3,4,5,6, listas para que el programa tome decisiones
    sumaus,cuanto tiene el usuario de envido
    sumacpu, cuanto tiene el programa de envido
    canto, respuestas del usuario
    PUNTOSU,PUNTOSC, puntos del usuario y del programa obtenidos en el envido

    Resultados (si la función devuelve):
    PUNTOSU,PUNTOSC,canto
    
    '''
    decision=['SI','NO']#50-50
    decision2=['SI','NO','SI','SI']#75-25
    decision3=['SI','NO','SI','SI','SI','SI','SI','SI','SI','SI']#90-10
    decision4=['SI','NO','NO','NO']#25-75
    decision5=['SI','NO','NO','NO','NO','NO','NO','NO','NO','NO']#10-90
    decision6=['NO']

    sumaus=uenv(UEC)
    sumacpu=uenv(CEC)
    PUNTOSU=0
    PUNTOSC=0

    
    print('\nResponde "E o "e" para envido, "R" o "r" para real envido y "F" o "f" para falta envido, si no desea hacerlo, responda "N" o "n"')
    canto=input('\nDesea cantar?: ')
    if canto=='E' or canto=='e': #envido
        print('El usuario canta ENVIDO')
        if sumacpu<24:
            shuffle(decision4)
            respuesta=decision4[0]
            if respuesta == 'NO':#envido no querido
                print('El programa no acepta')
                PUNTOSU+=1
            if respuesta =='SI': #envido querido
                print('El programa QUIERE')
                print (f'El usuario tiene {sumaus} de envido')
                if sumaus>=sumacpu:
                    print('El programa dice que son buenas')
                    PUNTOSU+=2
                if sumaus<sumacpu:
                    print (f'El programa tiene {sumacpu} de envido')
                    PUNTOSC+=2
        elif sumacpu>=24 and sumacpu<=29:
            shuffle(decision2)
            respuesta=decision2[0]
            if respuesta == 'SI':
                print('El programa QUIERE')#envido querido
                print (f'El usuario tiene {sumaus} de envido')
                if sumaus>=sumacpu:
                    print('El programa dice que son buenas')
                    PUNTOSU+=2
                if sumaus<sumacpu:
                    print (f'El programa tiene {sumacpu} de envido')
                    PUNTOSC+=2                    
            if respuesta =='NO':
                print('El programa canta ENVIDO')#envido envido
                print('\nResponde "SI" o "si" para aceptar, "R" o "r" para cantar real envido, "F" o "f" para falta envido, si no desea cantar nada y tampoco aceptar, responda "NO" o "no"')
                canto=input('\nRespuesta del usuario: ')
                if canto=='NO' or canto=='no':#envido envido no aceptado
                    PUNTOSC+=2
                    print('El usuario no acepta')
                if canto=='SI' or canto=='si':#envido envido aceptado
                    print('El usuario acepta')                        
                    print (f'El programa tiene {sumacpu} de envido')
                    if sumaus>=sumacpu:
                        print (f'El usuario tiene {sumaus} de envido')
                        PUNTOSU+=4
                    if sumaus<sumacpu:
                        print('El usuario dice que son buenas')
                        PUNTOSC+=4
                if canto=='R' or canto=='r':#envido envido real envido
                    print('El usuario canta REAL ENVIDO')
                    shuffle(decision5)
                    respuesta=decision5[0]
                    if respuesta=='SI':
                        print('El programa acepta')#envido envido real envido aceptado
                        print (f'El usuario tiene {sumaus} de envido')
                        if sumaus>=sumacpu:
                            print('El programa dice que son buenas')
                            PUNTOSU+=7
                        if sumaus<sumacpu:
                            print (f'El programa tiene {sumacpu} de envido')
                            PUNTOSC+=7
                              
                    if respuesta=='NO':#envido real envido no aceptado
                        print('El programa NO acepta')
                        PUNTOSU+=5
                if canto=='f' or canto=='F':#envido envido falta envido no aceptado
                    print('El usuario canta FALTA ENVIDO')
                    print('El programa no acepta')
                    PUNTOSU+=4

        elif sumacpu>=30 and sumacpu<=33:
            shuffle(decision4)
            respuesta=decision4[0]
            if respuesta == 'SI':
                print('El programa QUIERE')#envido querido
                print (f'El usuario tiene {sumaus} de envido')
                if sumaus>=sumacpu:
                    print('El programa dice que son buenas')
                    PUNTOSU+=2
                if sumaus<sumacpu:
                    print (f'El programa tiene {sumacpu} de envido')
                    PUNTOSC+=2                    
            if respuesta =='NO':
                print('El programa canta ENVIDO')#envido envido
                print('\nResponde "SI" o "si" para aceptar, "R" o "r" para cantar real envido, "F" o "f" para falta envido, si no desea cantar nada y tampoco aceptar, responda "NO" o "no"')
                canto=input('\nRespuesta del usuario: ')
                if canto=='NO' or canto=='no':#envido envido no aceptado
                    PUNTOSC+=2
                    print('El usuario no acepta')
                if canto=='SI' or canto=='si':#envido envido aceptado
                    print('El usuario acepta')                        
                    print (f'El programa tiene {sumacpu} de envido')
                    if sumaus>=sumacpu:
                        print (f'El usuario tiene {sumaus} de envido')
                        PUNTOSU+=4
                    if sumaus<sumacpu:
                        print('El usuario dice que son buenas')
                        PUNTOSC+=4
                if canto=='R' or canto=='r':#envido envido real envido
                    print('El usuario canta REAL ENVIDO')
                    shuffle(decision2)
                    respuesta=decision2[0]
                    if respuesta=='SI':
                        shuffle(decision6)
                        respuesta=decision6[0]
                        if respuesta=='NO':
                            print('El programa acepta')#envido envido real envido aceptado
                            print (f'El usuario tiene {sumaus} de envido')
                            if sumaus>=sumacpu:
                                print('El programa dice que son buenas')
                                PUNTOSU+=7
                            if sumaus<sumacpu:
                                print (f'El programa tiene {sumacpu} de envido')
                                PUNTOSC+=7
                                
                    if respuesta=='NO':#envido envido real envido no aceptado
                        print('El programa NO acepta')
                        PUNTOSU+=5
                if canto=='f' or canto=='F':
                    print('El usuario canta FALTA ENVIDO')
                    print('El programa no acepta')
                    PUNTOSU+=4
                                                        
    if canto=='R' or canto=='r':
        print('El usuario canta REAL ENVIDO\n')
        if sumacpu<25:
            shuffle(decision5)
            resultado=decision5[0]
            if resultado=='SI':
                print('El programa acepta')
                print (f'El usuario tiene {sumaus} de envido')
                if sumaus>=sumacpu:
                    print('El programa dice que son buenas')
                    PUNTOSU+=3
                if sumaus<sumacpu:
                    print (f'El programa tiene {sumacpu} de envido')
                    PUNTOSC+=3
            else:
                print('El programa no acepta')
                PUNTOSU+=1
                
        if sumacpu>=25 and sumacpu<=29:
            shuffle(decision4)
            resultado=decision4[0]
            if resultado=='SI':
                print('El programa acepta')
                print (f'El usuario tiene {sumaus} de envido')
                if sumaus>=sumacpu:
                    print('El programa dice que son buenas')
                    PUNTOSU+=3
                if sumaus<sumacpu:
                    print (f'El programa tiene {sumacpu} de envido')
                    PUNTOSC+=3
            else:
                print('El programa no acepta')
                PUNTOSU+=1
        if sumacpu>=30:
            shuffle(decision6)
            resultado=decision6[0]
            if resultado=='NO':
                print('El programa acepta')
                print (f'El usuario tiene {sumaus} de envido')
                if sumaus>=sumacpu:
                    print('El programa dice que son buenas')
                    PUNTOSU+=3
                if sumaus<sumacpu:
                    print (f'El programa tiene {sumacpu} de envido')
                    PUNTOSC+=3
                    
    if canto=='F' or canto=='f':
        print('El usuario canta FALTA ENVIDO\n')
        print('El programa no acepta')
        PUNTOSU+=1
        
    return PUNTOSU,PUNTOSC,canto

def envidocpu(UEC,CEC,primero):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    UEC,CEC,primero
    
    Objetivo (descripción de lo que hace o devuelve):
    para el envido si inicia el programa
    
    Síntesis de Casos (composición de casos para la generalización):
    se crea una herramienta para la toma de decisiones
    PUNTOSU es 0
    PUNTOSC es 0
    creamos la variable CANTO
    sumaus=uenv(UEC)
    sumacpu=uenv(CEC)
    si el programa tiene entre 25 y 33
        canta envido
        espera respuesta del usuario
        la respuesta se almacena en canto
        si es no
             el usuario no acepta
        si es si
            acepta
        si canto real envido, espero decision del programa en base a la herramienta de arriba
            si es si
                 el programa acepta
            si es no
                el programa no acepta
        si canto falta envido
            el programa no acepta
            CANTO es n
    sino
        CANTO es NOPA
        
    Recursos (variables o funciones internas -nombre y propósito)
    decision,2,3,4,5,6, listas para que el programa tome decisiones
    PUNTOSU,PUNTOSC, puntos del usuario y del programa obtenidos en el envido
    CANTO, variable para saber si alguien canto envido o no
    sumaus,cuanto tiene el usuario de envido
    sumacpu, cuanto tiene el programa de envido
    
    Resultados (si la función devuelve):
    PUNTOSU,PUNTOSC,CANTO
    
    '''
    decision=['SI','NO']#50-50
    decision2=['SI','NO','SI','SI']#75-25
    decision3=['SI','NO','SI','SI','SI','SI','SI','SI','SI','SI']#90-10
    decision4=['SI','NO','NO','NO']#25-75
    decision5=['SI','NO','NO','NO','NO','NO','NO','NO','NO','NO']#10-90
    decision6=['NO']

    PUNTOSU=0
    PUNTOSC=0
    CANTO=''

    sumaus=uenv(UEC)
    sumacpu=uenv(CEC)   

    if sumacpu>25 and sumacpu<=33:
        print('El programa canta ENVIDO')
        print('\nResponde "SI" o "si" para aceptar, "r" o "R" para cantar real envido, "F" o "f" para cantar falta envido o responda "N" o "n" para no hacerlo')
        canto=input('\nRespuesta del usuario: ')
        if canto=='N' or canto=='n':
            print('El usuario no acepta')
            PUNTOSC+=1
        if canto=='SI' or canto=='si':
            print (f'El programa tiene {sumacpu} de envido')
            if sumaus>sumacpu:
                print (f'El usuario tiene {sumaus} de envido')
                PUNTOSU+=2
            if sumaus<=sumacpu:
                print('El usuario dice que son buenas')
                PUNTOSC+=2
        if canto=='r' or canto=='R':
            shuffle(decision4)
            resultado=decision4[0]
            if resultado=='SI':
                print('El programa acepta')
                print (f'El usuario tiene {sumaus} de envido')
                if sumaus>=sumacpu:
                    print('El programa dice que son buenas')
                    PUNTOSU+=5
                if sumaus<sumacpu:
                    print (f'El programa tiene {sumacpu} de envido')
                    PUNTOSC+=5
            if resultado=='NO':
                print('El programa no acepta')
                PUNTOSU+=2
        if canto=='f' or canto== 'F':  
            print('El programa no acepta')
            PUNTOSU+=2
            CANTO='n'
    else:
        CANTO='NOPA'

    return PUNTOSU,PUNTOSC,CANTO

def uenv(cartas):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    recibe cartas que es un parametro que puede ser UEC o CEC
    
    Objetivo (descripción de lo que hace o devuelve):
    obtener cuanto tiene el programa uy el usuario de envido
    
    Síntesis de Casos (composición de casos para la generalización):
    inicializo lista
    si el tipo de la carta 1 es igual al de la 2 e igual al de la 3
        agregar valor de carta 1,2,3 en lista
        ordenar lista de mayor a menor
        suumar los dos primeros elemento y sumarle 20
    si el tipo de la carta 1 es igual al de la 2 pero el tipo de carta 1 es distinto al de la 3
        agregar valor de carta 1,2 en lista
        suumar los dos primeros elemento y sumarle 20
    si las tres cartas son distintas
        agregar valor de carta 1,2,3 en lista
        ordenar lista de mayor a menor
        obtener mayor     
    si el tipo de la carta 2 es igual al de la 3 pero el tipo de carta 1 es distinto al de la 2
        agregar valor de carta 3,2 en lista
        suumar los dos primeros elemento y sumarle 20
    si el tipo de la carta 1 es igual al de la 3 pero el tipo de carta 3 es distinto al de la 2
        agregar valor de carta 3,1 en lista
        suumar los dos primeros elemento y sumarle 20
        
    Recursos (variables o funciones internas -nombre y propósito)
    cartas[1],cartas[3],cartas[5], los tipos de simbolo de las cartas
    lista,lista para alacenar cartas seleccionadas
    
    Resultados (si la función devuelve):
    suma
    
    '''
    lista=[]
    if cartas[1]==cartas[3] and cartas[1]==cartas[5]:
        lista.append(cartas[0])
        lista.append(cartas[2])
        lista.append(cartas[4])
        lista.sort(reverse=True)
        suma=(int(lista[0]))+(int(lista[1]))+20
    if cartas[1]==cartas[3] and cartas[1]!=cartas[5]:
        lista.append(cartas[0])
        lista.append(cartas[2])
        suma=(int(lista[0]))+(int(lista[1]))+20
    if cartas[1]!=cartas[3] and cartas[1]!=cartas[5] and cartas[3]!=cartas[5]:
        lista.append(cartas[0])
        lista.append(cartas[2])
        lista.append(cartas[4])
        lista.sort(reverse=True)
        suma=(int(lista[0]))
    if cartas[1]!=cartas[3] and cartas[3]==cartas[5]:
        lista.append(cartas[2])
        lista.append(cartas[4])
        suma=(int(lista[0]))+(int(lista[1]))+20
    if cartas[1]==cartas[5] and cartas[3]!=cartas[5]:
        lista.append(cartas[0])
        lista.append(cartas[4])
        suma=(int(lista[0]))+(int(lista[1]))+20

    return suma


        
'''--------------------------------------------------------------------------------------------PROGRAMA PRINCIPAL--------------------------------------------------------------------------------------------------------------------------'''
# PROGRAMA    
#1 PRÓLOGO
#1.1 Presentación
#1.1.1 Impresión del título del programa en pantalla
print('\n                                                  Truco: El gran juego argentino\n')

#1.1.2 Descripción o aclaraciones al usuario (opcional)
print('\'SI\' si desea iniciar, \'No\' si desea terminar')
#1.2 Datos iniciales 
#1.2.1 Solicitud e ingreso de datos desde teclado (opcional, si los datos se piden durante la resolución)
inicio=input('Desea iniciar el juego?: ')
print()
#1.2.2 Establecimiento de valores iniciales para datos auxiliares o que se transformarán en resultados (opcional)
PUNTOSU=0
PUNTOSC=0
PU=0
PC=0
from random import choice
from random import shuffle
primero=choice(['TU INICIAS','INICIA EL PROGRAMA'])

#2 RESOLUCIÓN
# Descomposición del problema en subproblemas 2.x que a su vez pueden requerir ingreso o inicialización de datos o mostrar resultados
while inicio=='si' or inicio=='SI':
    while PU<=30 and PC<=30:
        if PU>=30 and PC<30:
            print('GANASTE LA PARTIDA, FELICITACIONES')
        if PU<30 and PC>=30:
            print('LAMENTABLEMENTE PERDISTE')
        while inicio=='SI' or inicio== 'si':
            contador=1
            manos_usuario1=0
            manos_usuario2=0
            manos_usuario3=0
            manos_usuario4=0
            manos_usuario5=0
            manos_usuario6=0

            manos_cpu1=0
            manos_cpu2=0
            manos_cpu3=0
            manos_cpu4=0
            manos_cpu5=0
            manos_cpu6=0
            
            mazo=mazos()
            Umsp,Ump,Cmsp,Cmp=cartas(mazo)
            print('\nSe sortea quien inicia...')
            print(f'{primero}\n')
            print('\n                                                                               MANO N1\n')
            UEC,CEC=valores(Umsp,Cmsp)
            
            manos_usuario1,manos_cpu1,Cmsp,Umsp,Cmp,Ump,PUNTOSU,PUNTOSC,contador,PuntoU,PuntoC=juego(primero,Umsp,Ump,Cmsp,Cmp,UEC,CEC,PUNTOSU,PUNTOSC)#juego


            PU+=PuntoU
            PC+=PuntoC
            if contador!=99:
            
                if manos_usuario1==1 and manos_cpu1==0:#1-0
                    print('\n                                                                           SIGUIENTE MANO\n')
                    manos_usuario2,manos_cpu2,Cmsp,Umsp,Cmp,Ump=MANOUS(Cmsp,Cmp,Umsp,Ump,manos_usuario1,manos_cpu1)#MANOUS

                if manos_usuario2==2 and manos_cpu2==0:#1-0 2-0
                    print('GANASTE LA MANO')
                    if contador==1:
                        PU+=1
                    elif contador==2:
                        PU+=2
                    elif contador==3:
                        PU+=3
                    elif contador==4:
                        PU+=4
                if manos_usuario1==0 and manos_cpu1==1:#0-1
                    print('\n                                                                           SIGUIENTE MANO\n')
                    manos_usuario3,manos_cpu3,Cmsp,Umsp,Cmp,Ump=MANOCPU(Cmsp,Cmp,Umsp,Ump,manos_usuario1,manos_cpu1)#MANOCPU
                    
                if manos_usuario3==0 and manos_cpu3==2:#0-1 0-2
                    print('PERDISTE LA MANO')
                    if contador==1:
                        PC+=1
                    elif contador==2:
                        PC+=2
                    elif contador==3:
                        PC+=3
                    elif contador==4:
                        PC+=4

                if manos_usuario1==1 and manos_cpu1==1:#1-1
                    print('\n                                                                           SIGUIENTE MANO\n')
                    if primero=='TU INICIAS':
                        manos_usuario4,manos_cpu4,Cmsp,Umsp,Cmp,Ump=MANOUS(Cmsp,Cmp,Umsp,Ump,manos_usuario1,manos_cpu1) #MANOUS
                      
                    if primero=='INICIA EL PROGRAMA':
                        manos_usuario4,manos_cpu4,Cmsp,Umsp,Cmp,Ump=MANOCPU (Cmsp,Cmp,Umsp,Ump,manos_usuario1,manos_cpu1)#MANOCPU

                if manos_usuario2==1 and manos_cpu2==1:#1-0 1-1
                    print('\n                                                                           SIGUIENTE MANO\n')#GANO,PIERDO
                    manos_usuario5,manos_cpu5,Cmsp,Umsp,Cmp,Ump=MANOCPU (Cmsp,Cmp,Umsp,Ump,manos_usuario2,manos_cpu2)#MANOCPU
                    if manos_usuario5==2 and manos_cpu5==2:
                        print('\nGANASTE LA MANO')
                        if contador==1:
                            PU+=1
                        elif contador==2:
                            PU+=2
                        elif contador==3:
                            PU+=3
                        elif contador==4:
                            PU+=4
                        
                if manos_usuario3==1 and manos_cpu3==1:#0-1 1-1
                    print('\n                                                                           SIGUIENTE MANO\n')#PIERDO,GANO
                    Cmsp,Cmp,Umsp,Ump,manos_usuario5,manos_cpu5=MANOUSUARIO (Cmsp,Cmp,Umsp,Ump,manos_usuario3,manos_cpu3)#MANOCPU
                    if manos_usuario5==2 and manos_cpu5==2:
                        print('\nPERDISTE LA MANO')
                        if contador==1:
                            PC+=1
                        elif contador==2:
                            PC+=2
                        elif contador==3:
                            PC+=3
                        elif contador==4:
                            PC+=4
                            
                
                if manos_usuario3==1 and manos_cpu3==2:#0-1 1-2
                    print('\nPERDISTE LA MANO')
                    if contador==1:
                        PC+=1
                    elif contador==2:
                        PC+=2
                    elif contador==3:
                        PC+=3
                    elif contador==4:
                        PC+=4
                if manos_usuario2==2 and manos_cpu2==1:#1-0 2-1
                    print('\nGANASTE LA MANO')
                    if contador==1:
                        PU+=1
                    elif contador==2:
                        PU+=2
                    elif contador==3:
                        PU+=3
                    elif contador==4:
                        PU+=4                
                if manos_usuario4==1 and manos_cpu4==2:#1-1 1-2
                    print('\nPERDISTE LA MANO')
                    if contador==1:
                        PC+=1
                    elif contador==2:
                        PC+=2
                    elif contador==3:
                        PC+=3
                    elif contador==4:
                        PC+=4
                if manos_usuario4==2 and manos_cpu4==1:#1-1 2-1
                    print('\nGANASTE LA MANO')
                    if contador==1:
                        PU+=1
                    elif contador==2:
                        PU+=2
                    elif contador==3:
                        PU+=3
                    elif contador==4:
                        PU+=4                
                if manos_usuario5==1 and manos_cpu5==2:#1-0 1-1 1-2
                    print('\nPERDISTE LA MANO')
                    if contador==1:
                        PC+=1
                    elif contador==2:
                        PC+=2
                    elif contador==3:
                        PC+=3
                    elif contador==4:
                        PC+=4
                if manos_usuario5==2 and manos_cpu5==1:#1-0 1-1 2-1
                    print('\nGANASTE LA MANO')
                    if contador==1:
                        PU+=1
                    elif contador==2:
                        PU+=2
                    elif contador==3:
                        PU+=3
                    elif contador==4:
                        PU+=4   
                if manos_usuario4==2 and manos_cpu4==2:#1-1 2-2
                    if primero=='TU INICIAS':
                        Cmsp,Cmp,Umsp,Ump,manos_usuario6,manos_cpu6=MANOUSUARIO(Cmsp,Cmp,Umsp,Ump,manos_usuario4,manos_cpu4) #MANOUSUARIO
                    else:
                        manos_usuario6,manos_cpu6,Cmsp,Umsp,Cmp,Ump=MANOCPU (Cmsp,Cmp,Umsp,Ump,manos_usuario4,manos_cpu4)#MANOCPU
                if manos_usuario6==3 and manos_cpu6==2:#1-1 2-2 3-2
                        print('\nGANASTE LA MANO')
                        if contador==1:
                            PU+=1
                        elif contador==2:
                            PU+=2
                        elif contador==3:
                            PU+=3
                        elif contador==4:
                            PU+=4                       
                if manos_usuario6==2 and manos_cpu==3:#1-1 2-2 2-3
                        print('\nPERDISTE LA MANO')
                        if contador==1:
                            PC+=1
                        elif contador==2:
                            PC+=2
                        elif contador==3:
                            PC+=3
                        elif contador==4:
                            PC+=4   
                if manos_usuario6==3 and manos_cpu6==3:        
                    if primero=='TU INICIAS':
                        print('\nGANASTE LA MANO')
                        if contador==1:
                            PU+=1
                        elif contador==2:
                            PU+=2
                        elif contador==3:
                            PU+=3
                        elif contador==4:
                            PU+=4                           
                    else:
                        print('\nPERDISTE LA MANO')
                        if contador==1:
                            PC+=1
                        elif contador==2:
                            PC+=2
                        elif contador==3:
                            PC+=3
                        elif contador==4:
                            PC+=4                           
            if contador==1000 or contador==5000:
                PC+=1
            if contador==4000:
                PU+=1
                
            print(f'\nEl usuario tiene {PU} puntos')
            print(f'El programa tiene {PC} puntos')
            TERMINADO=0

            
            if PU>=30 and PC<30:
                print('GANASTE LA PARTIDA, FELICITACIONES')
                TERMINADO=30
            if PU<30 and PC>=30:
                print('LAMENTABLEMENTE PERDISTE')
                TERMINADO=30
                
            if TERMINADO==0:
                print('\n\'SI\' si desea iniciar, \'No\' si desea terminar')
                inicio=input('Desea continuar con el juego?: ')
                if primero=='TU INICIAS':
                    primero='INICIA EL PROGRAMA'
                else:
                    primero='TU INICIAS'
                    
            if TERMINADO==30:
                print('\n\'SI\' si desea iniciar, \'No\' si desea terminar')
                inicio=input('Desea continuar con el juego?: ')
                if primero=='TU INICIAS':
                    primero='INICIA EL PROGRAMA'
                else:
                    primero='TU INICIAS'
                PU=0
                PC=0
                print(f'\nEl usuario tiene {PU} puntos')
                print(f'El programa tiene {PC} puntos')
#3 EPÍLOGO
#3.1 Muestra de la solución del problema por pantalla (opcional, si sólo se muestran resultados durante la resolución)

#3.2 Pausa para ver resultados en pantalla que se puede obviar, si los resultados se van mostrando durante la resolución
print() # salto de línea
input('Pulse tecla Enter para terminar el programa...') # pausa forzada
