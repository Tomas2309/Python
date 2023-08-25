'''
Objetivo del programa (descripción del problema que resuelve):
Armar un prototipo del programa para cargar la matriz ampliada del sistema y que los muestre en pantalla,
más otro prototipo incremental que  halle la inversa de A o concluya que es singular y lo reporte en pantalla
Ademas un prototipo incremental que busque la solución del sistema e informe el resultado en pantalla, más prototipo 
incremental que almacene el resultado en un archivo de texto


Autor/es: Tomas Aguirre, Menchaca Miguel Ángel, Paulo Sosa

Versión:1 

Fecha: 21-11-21

Análisis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba del programa):
1.
{matriz ampliada}

  [2][1][2][2][3]
  [1][1][3][4][2]===> La matriz A=[2][1][2][2] es CUADRADA, por lo que calculamos el determinante = 8 ===> Matriz escalonada=[2.0][1.0][2.0][2.0][3.0]
  [4][3][2][6][3]                 [1][1][3][4]                                                                               [0.0][5.0][2.0][3.0][0.5]
  [1][2][3][6][7]                 [4][3][2][6]                                                                               [0.0][0.0][-6.0][-4.0][-4.0]
                                  [1][2][3][6]                                                                               [0.0][0.0][0.0][-1.3][6.66]
      
2.
{matriz ampliada}
  [5][5][3] =======> La matriz A=[5][5] es CUADRADA, por lo que calculamos el determinante = 0 =========> Matriz singular 'no tiene Matriz inversa'
  [5][5][6]                      [5][5]


3.
{matriz ampliada}
  [1][2][3] =======> La matriz A=[1][2] no es CUADRADA, por lo que =========> 'No tiene Matriz inversa'
  [4][5][6]                      [6][5]                                                                                    
  [1][2][3]                      [1][2]     
  
Síntesis de Casos (composición de casos para la generalización):
-Solicitar al usuario el nombre del archivo con la matriz ampliada y guardarlo en nombre
-obtener matriz ampliada, matriz cuadrada y matriz de terminos independientes proveniente de la funcion cargar
-imprimir matriz ampliada en punto flotante en formato de lista
-calcular la determinante de la matriz cuadrada. 
-si la determinante es cero, la matriz es singular y luego se determina si es incompatible o no
-Sino, continua el programa
    -El sistema es compatible determinado
    -Escalonar matriz ampliada y obtener como resultado las incognitas del sistema de ecuacion
    -Si la matriz es 2x2,3x3 o 4x4
        -Imprimir valores de incognitas en punto flotante como lista
        -Guarda y exportar los resultados de las incognitas del sistema y su precision en un archivo txt externo al programa
        
Recursos (variables y funciones del programa -nombre y propósito)

    Datos a solicitar al usuario (sea en el prólogo o sea durante la resolución):
    nombre, nombre de archivo de texto con matriz ampliada

    Auxiliares (necesarios para transformaciones intermedias):
    Mamp, matriz ampliada
    BB, matriz de terminos independientes
    AA, matriz cuadrada que contiene las filas y columnas menos la ultima columna que contiene los terminos independientes

    Resultados (a informar sea durante el desarrollo o en el epílogo):
    det, valor de la determinante en punto flotante
    esca, matriz escalonada 
    INC, valores de las incognitas del sistema de ecuaciones linealmente dependiente 
    
    Funciones propias (necesarias para la descomposición del problema en subproblemas):

    def cargar, funcion para la carga del archivo de texto. Devuelve Ma,AA,BB y sus variables en el programa principal son Mamp, AA y BB respectivamente

    def determinante, funcion para calcular la determinante de A. Devuelve suma y su variable en el programa principal es det

    def gauss, funcion para calcular la matriz escalonada (metodo de gauss)

    def incognitas, funcion para calcular las incognitas a partir de los resultados de la funcion gauss

    def si, determina si el sistema es incompatible 

    def guardar, funcion para la devolucion de resultados en un archivo de texto eterno al programa
    
    
    
'''
# DEFINICIÓN DE FUNCIONES (si se requieren para descomponer la solución del problema)

'''=======================================================FUNCIONES============================================='''

def cargar(ar):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    ar, nombre de archivo de texto
    
    Objetivo (descripción de lo que hace o devuelve):
    Lee una matriz ampliada de n filas y n+1 columnas. Luego devuelve la matriz ampliada en filas y columnas, la matriz cuadrada en forma de lista
    y la columna de terminos independientes en forma de lista
    
    Sintesis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba
    de la función):
    Abrir ar para lectura en archivo
    inicializar ma,AA,BB como listas vacias
    para linea en archivo
        dividimos cada valor de la matriz en partes y lo almacenamos en linea
        para i desde cero a longitud de linea
            transformamos cada valor de linea en punto flotante
            almacenamos en A los valores de linea menos la ultima columna
        agrego en la lista AA lo almacenado en A
        agrego en la lista ma lo almacenado en linea
    obtengo la cantidad de filas y columnas de ma
    almaceno en B los valores de la ultima columna la matriz
    agrego en la lista BB lo almacenado en B
    cierro archivo
    devuelvo ma,AA,BB        

    Recursos (variables o funciones internas -nombre y propósito)
    archivo, se almacena el txt ingresado
    cf, cantidad de filas
    cc, cantidad de columnas

    Auxiliares (necesarios para transformaciones intermedias):
    linea, se almacenan en linea cada valor de la matriz en partes
    A, almacenamos en A los valores de linea menos la ultima columna
    B, almaceno en B los valores de la ultima columna la matriz

        
    Resultados (si la función devuelve):
    ma, matriz ampliada
    AA, matriz cuadrada
    BB, columna de terminos indepedientes
    cf, cantidad de filas de matriz ampliada

    '''
    #1 PRÓLOGO
    # Establecimiento de valores iniciales para datos auxiliares o que se transformarán en resultados (opcional)
    archivo=open(ar,'r')
    ma=[]
    AA=[]
    BB=[]
    
    for linea in archivo:
        linea=linea.split()
        for i in range(len(linea)):
            linea[i]=float(linea[i])
            A=linea[:-1]#Para eliminar ultima columna de Mampliada
        AA.append(A)
        ma.append(linea)

    cf=len(ma) #CANTIDAD DE FILAS
    cc=int(len(ma[0])) #CANTIDAD DE COLUMNAS

    B = [fila[cc-1] for fila in ma]  #ULTIMA COLUMNA
    BB.append(B)
    
    archivo.close()
    return ma,AA,BB,cf

def determinante(m):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    m, matriz cuadrada AA en forma de lista
    
    Objetivo (descripción de lo que hace o devuelve):
    Lee una matriz cuadrada en forma de lista y devuelve la determinante de la matriz

    Sintesis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba
    de la función):
    calcular la cantidad de filas que tiene la matriz
    si tiene 2 filas
        devuelve el resultado de multiplicar el valor de la posicion[0][0] con el valor de la posicion[1][1] y restarlo por el valor
         en [1][0] multiplicado por [0][1]
    sino
        configuramos para que suma almacene los resultados en punto flotante
        para f en el rango de 0 a cantidad de filas
            si la matriz en columna 0, y filas desde 0 a cantidad de filas es igual a 0.0
            inicializamos adjunta como lista vacia
            para f2 de 0 a cantidad de fila
                si f2 es distinto de f
                    agrego a la lista 'adjunta' los valores de las posiciones q vaya tomando f2(en cuanto a la fila) y subiendo de 1 en uno los de la columna
            si f es par
                la variable suma almacena los resultados de hacer suma mas el resultado de multiplicar la posicion f en fila y 0 en columna por la
                funcion recursiva determinante con el parametro formal 'adjunta'
            sino
                la variable suma almacena los resultados de hacer suma menos el resultado de multiplicar la posicion f en fila y 0 en columna por la
                funcion recursiva determinante con el parametro formal 'adjunta'
        devuelve suma
    
    Análisis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba
    de la función):
    1. [2][3]======> determinante 2X2 = 14
       [1][9]

    2. [1][1]=====> determinante 2X2 = 0
       [1][1]

    3.[1][2][3]====> determinante no cuadrada(2X3) = no tiene determinante, matriz singular
      [12][3][4]

    Recursos (variables o funciones internas -nombre y propósito)
    cf, cantidad de filas de la matriz
    m, representa a la matriz cuadrada ingresada
    
    Auxiliares (necesarios para transformaciones intermedias):
    adjunta, lista donde se iran almacenando las posiciones de la matriz cuadrada
    f, valores auxiliares de 0 a cf
    f2, idem a f
    
    Resultados (si la función devuelve):
    suma, devuelve el resultado de la determinante de la matriz

    Funciones internas (necesarias para la descomposición del problema en subproblemas):
    determinante, funcion recursiva

    '''
    cf = len(m)    
    if cf==2: return m[0][0]*m[1][1]-m[1][0]*m[0][1]
    else:
        suma = 0.0
        for f in range(cf):
            if m[f][0]!=0.0:
                adjunta = []
                for f2 in range(cf):
                    if f2!=f: adjunta.append(m[f2][1:])

                if f%2==0: suma += m[f][0]*determinante(adjunta)
                else: suma -= m[f][0]*determinante(adjunta)
        return suma    

def gauss(m):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    m, matriz ampliada Mamp en forma de lista
    
    Objetivo (descripción de lo que hace o devuelve):
    recibe la matriz ampliada y devuelve la matriz escalonada (triangular superior)

    Sintesis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba
    de la función):
    obtener ultima fila
    obtener ultima columna
    constante b es igual a 0(luego se ira incrementando de 1 en 1)
    para i en el rango de 0 a ultima fila
        para c en el rango de 0 a ultima columna menos 1 menos b
            si el valor de la matriz ampliada en la posicion ufila menos c menos 1 y columna i es 0 o el valor de la fila
            de la matriz es ufila menos c y columna i es 0
                factor es igual a 0
            sino factor es igual a la posicion ufila menos c (fila) y columna igual a i(columna). Esto dividido la posicion
            ufila menos c menos 1 y columna i
            para k en el rango de 0 a ucol mas 1
                la posicion ufila menos c menos 1 y columna k de la matriz menos igual a la posicion ufila menos c menos 1
                y columna k multiplicado por factor
        le sumo uno a b
    devuelve m    


    Análisis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba
    de la función):
    1.[2][1][2][2][3]                   [2][1][2]  [2] [3]
      [1][1][3][4][2]=============>     [0][5][2]  [3][0.5]
      [4][3][2][6][3]                   [0][0][-6][-4] [-4]
      [1][2][3][6][7]                   [0][0][0][-1.3][6.6]

    Recursos (variables o funciones internas -nombre y propósito)
    ufila, ultima fila 
    ucol, ultima columna
    
    Auxiliares (necesarios para transformaciones intermedias):
    factor, transformacion a 0
    i,valores de 0 a ufila
    c,valores de 0 a ucol-1-b
    k,valores de 0 a ucol+1
    b,variable incremental de 1 a 1
    
    Resultados (si la función devuelve):
    m, matriz escalonada 

    '''
    ufila=len(m)-1
    ucol=len(m[0])-1
    b=0
    for i in range (0,ufila):
        for c in range(0,ucol-1-b):
            if m[ufila-c-1][i]==0 or m[ufila-c][i]==0:
                factor=0
            else:
                factor=m[ufila-c][i]/m[ufila-c-1][i]
            for k in range(0,(ucol+1)):
                m[ufila-c][k]-=(m[ufila-c-1][k]*factor)
        b+=1
        
    return m

def incognitas(m):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    m, matriz escalonada
    
    Objetivo (descripción de lo que hace o devuelve):
    recibe matriz escalonada y devuelve los valores de las incognitas de los sistemas de ecuaciones

    Sintesis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba de la función):
    inicializar VV como lista vacia
    inicializar RES como lista vacia
    obtenemos ultima fila y ultima columna de la matriz escalonada
    obtenemos el valor de la anteultima columna de la ultima fila y lo almacenamo en inc
    almaceno en V la columna independiente de la matriz escalonada
    almacena en VV la columna almacenada en V
    obtengo ultima fila y ultima columna de VV
    inicializo la variable acum en 0
    si acum es menor igual a ucol
        si inc es 0
            a es igual a 0
        sino
            a es igual a la fila 0 y columna ucol menos acum de VV dividido inc
        almaceno en RES lo almacenado en a
        le sumo uno a acum
        si acum es menor igual a ucol
            si la posicion en ufila -2(fila) y ucol-1(columna) de m es 0
                b es igual a 0
            sino
                b es igual a la fila 0 y columna ucol menos acum de VV menos el valor a multiplicado por el valor en ufila menos 2 y columna ucol de m.
                Todo eso dividido la posicion en ufila -2(fila) y ucol-1(columna) de m
            almaceno b en RES
            le sumo uno a acum
            continuo hasta almacenar un valor de d
    luego invierto la lista y almaceno los resultados en RES
    devuelvo RES
     
    Recursos (variables o funciones internas -nombre y propósito)
    VV, lista con la columna independiente de la matriz escalonada
    ufilaESC, ultima fila de la matriz escalonada
    ucolESC,ultima columna de la matriz escalonada
    inc, valor anteultima columna de ultima fila
    ucol, ultima columna de VV
    ufila, ultima fila de VV
    acum, acumulador. A medida que obtenemos una incognita incrementamos en uno la variable acum
    a,b,c,d., resultado de la incognita
    
    Resultados (si la función devuelve):
    RES, lista con los valores de las incognitas
    a,b,c,d, resultados de incognitas 
    
    '''
    VV=[]
    RES=[]
    ufilaESC=len(m)-1
    ucolESC=len(m[0])-1
    inc=(m[ufilaESC][ucolESC-1]) #valor anteultima columna de ultima fila
    V = [fila[ucolESC] for fila in m]
    VV.append(V)#columna independiente    
    ufila=len(VV)-1 
    ucol=len(VV[0])-1    
    acum=0
    if acum<=ucol:        
        if inc==0:
            a==0
        else:
            a=(VV[0][ucol-acum])/inc
        RES.append(a)#resultado incognitas
        acum+=1            
        if acum<=ucol:
            if (m[ufila-2][ucol-1])==0:
                b==0
                c==0
                d==0
            else:
                b=((VV[0][ucol-acum])-(a*(m[ufila-2][ucol])))/(m[ufila-2][ucol-1])
                c=0
                d=0
            RES.append(b)#resultado incognitas
            acum+=1#2
        if acum<=ucol:            
            if (m[ufila-3][ucol-2])==0:
                c==0
                d==0
            else:
                c=((VV[0][ucol-acum])-(a*(m[ufila-3][ucol]))-(b*(m[ufila-3][ucol-1])))/(m[ufila-3][ucol-2])
                d==0
            RES.append(c)#resultado incognitas
            acum+=1#3
        if acum<=ucol:
            if (m[ufila-4][ucol-3])==0:
                d==0
            else:
                d=(((VV[0][ucol-acum]))-(c*(m[ufila-4][ucol-2]))-(b*(m[ufila-4][ucol-1]))-(a*(m[ufila-4][ucol])))/(m[ufila-4][ucol-3])
            RES.append(d)#resultado incognitas
    RES.reverse()
    return(RES,a,b,c,d)

def si(a,b,mamp):#Teorema de ROUCHÉ-FRÖBENIUS
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    a, matriz cuadrada
    b, columna de terminos independientes
    mamp, matriz ampliada

    Objetivo (descripción de lo que hace o devuelve):
    Determinar si el sistema es incompatible o no

    Sintesis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba
    de la función):
    calcular la cantidad de filas de la matriz cuadrada
    para i desde 0 a cantidad de filas menos uno
        la columna [i] de la matriz cuadrada va a ser igual a la unica columna de B
        si el determinante de la matriz cuadrada es distinto de 0
            el sistema es incompatible
        sino
            esa columna[i] de la matriz cuadrada vuelve a tener los valores originales
    '''

    cf=len(a)
    for i in range(0,cf-1):
        a[i]=b[0]
        if determinante(a)!=0:
            print('Sistema incompatible')
        else:
            a[i]=mamp[i]
    

def guardar(m,A,B,a,b,c,d):
    '''
    Recibe (descripción de parámetros de la función -tipo de valores-, si es que tiene):
    m, valores de las incognitas
    
    Objetivo (descripción de lo que hace o devuelve):
    recibe resultados de las incognitas y devuelve un archivo .txt externo al programa con los resultados

    Sintesis de Casos (número de caso, estado inicial, transformación, estado final -se consideran casos base para la prueba
    de la función):
    abrir un nuevo archivo .txt para sobreescribir los resultados de las incognitas
    obtener cantidad de filas de B(columna de terminos independientes de matriz ampliada)
    obtener cantida de columnas y filas de A(matriz cuadrada)
    inicializar lista PRE
    para i desde 0 a filaA mas uno
        si filaA es 1
            la precision de la ecuacion es: reemplazar las incognitas calculadas por las letras que representaban valores desconocidos y multiplicar
            cada coeficiente con su incognita calculada
            restar el valor que se encuentra en la misma fila pero en la columna de terminos indeptes. al valor de la suma de lo obtenido en el paso anterior
            almacenar en PRE los resultados de res
  
    transformar en cadena de caracteres los valores de m
    escribir titulo en .txt
    escribir informacion relevante en .txt
    hacer q el .txt contenga las soluciones
    hacer q el .txt contenga la precision de los valores de las incognitas 
    cerrar el archivo

    Recursos (variables o funciones internas -nombre y propósito)
    file, variable q contiene el nuevo .txt donde se exportara el programa
    m, variable donde se almacenaran los valores de m en cadena de caracteres
        
    Resultados (si la función devuelve):
    1_r.txt, nuevo txt con los resultados
    PRE, precision de la matriz

    '''
    file=open('1_r.txt','w')
    colB=len(B[0])-1#3
    filaA=len(A)-1#3
    colA=len(A[0])-1#3
    PRE=[]
    
    for i in range(0,filaA+1):
        if filaA==1:#matriz 2X2
            res=((B[0][i])-(((AA[i][1])*a)+((AA[i][0])*b)))
            PRE.append(res)
        if filaA==2:#matriz 3X3
            res=((B[0][i])-(((AA[i][2])*a)+((AA[i][1])*b)+((AA[i][0])*c)))
            PRE.append(res)
        if filaA==3:#matriz 4X4
            res=((B[0][i])-(((AA[i][3])*a)+((AA[i][2])*b)+((AA[i][1])*c)+((AA[i][0])*d)))
            PRE.append(res)
                    
    m=str(m)
    file.write('                                      RESULTADOS\n\n\n')
    file.write('Las incognitas apareceran desde x1 y se iran incrementando')
    file.write('\n\n'f'Las incognitas son: {m}')
    file.write('\n\n'f'La precision del resultado es: {PRE} para cada ecuacion del sistema') 
    
    file.close() 


'''=================================================PROGRAMA PRINCIPAL==========================================='''

#1 PRÓLOGO
#1.1.1 Impresión del título del programa en pantalla
print()
print(       '   ---------------------------------------------------------------------------')
print('              Calculo de incognitas de un sistema de ecuaciones')            
print(       '   ---------------------------------------------------------------------------\n')


#1.2 Datos iniciales 
#1.2.1 Solicitud e ingreso de datos desde teclado (opcional, si los datos se piden durante la resolución)

nombre=input('Ingrese el nombre del archivo con los datos: ')




#2 RESOLUCIÓN
# Descomposición del problema en subproblemas 2.x que a su vez pueden requerir ingreso o inicialización de datos o mostrar resultados

Mamp,AA,BB,CF=cargar(nombre)
print('\nLa matriz ampliada es: \n')
for fila in Mamp:
    print(fila)      #impresion de la matriz en filas y columnas
#print(Mamp)         #impresion de la matriz ampliada
#print(AA)           #impresion de la matriz cuadrada
#print(BB)           #impresion de la columna de terminos independientes


det=determinante(AA)
print(f'\nLa determinante de la matriz es {det}\n') #impresion del valor de la determinante de la matriz

if det==0.0:
    print('La matriz es singular\n') #si la determinante es 0, la matriz es singular
    si(AA,BB,Mamp)#sistema incompatible

else:
    print('El sistema es compatible determinado')
    esca=gauss(Mamp)
    #print(f'Matriz escalonada={esca}')#impresion de la matriz escalonada
    print()

    if CF==2 or CF==3 or CF==4:
        INC,a,b,c,d=incognitas(esca)
        print(f'Las incognitas son {INC}\n')#impresion de los valores de las incognitas obtenidas
        guardar(INC,AA,BB,a,b,c,d) #para exportar los resultados de las incognitas a un .txt



#3.2 Pausa para ver resultados en pantalla que se puede obviar, si los resultados se van mostrando durante la resolución
print() # salto de línea
input('Pulse tecla Enter para terminar el programa...') # pausa forzada
