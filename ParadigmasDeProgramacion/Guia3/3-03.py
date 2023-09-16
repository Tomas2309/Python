"""3. Menu de Opciones con secuencias Escribir un programa que le permita al usuario, a
través de un menú de opciones, las siguientes operaciones: a) Generar una serie n de
números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la suma de los
cuadrados b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras
que finalizan con vocales c) Ingresar una serie de números (la carga finaliza con cero) y
determinar si hay mayor cantidad de valores pares o de impares d) Salir """
import random,time;
def menu():
    print("""
    MENU DE OPCIONES

    a) Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la suma de los cuadrados
    b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales
    c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares
    d) Salir 

    """);
cuadrado=0;
menu();
opcion=(input("Ingrese 'a','b','c','d' de acuerdo a lo que desee realizar: ")).lower();
while opcion=='a' or opcion=='b' or opcion=='c':
    if opcion=='a':
        sumatoria=0;
        print("\na) Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la suma de los cuadrados\n");
        num=int(input("Ingrese cantidad de numeros a generar: "));
        for i in range(0,num):
            random_num=random.randint(1,100);
            cuadrado=(random_num)**2;
            sumatoria+=cuadrado;
            print(random_num);
            print(cuadrado);
        print(f'La sumatoria es {sumatoria}');
        time.sleep(1);
        menu();
        opcion=(input("Ingrese 'a','b','c','d' de acuerdo a lo que desee realizar: ")).lower();
    elif opcion=='b':
        contador=0;
        print("\nb) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales");
        time.sleep(1);
        texto=input("Ingrese un texto finalizado en un punto: ");
        texto=(texto.split('.'));
        texto=texto[0].split();
        for i in range(0,len(texto)):
            if texto[i][-1] in 'aeiou':
                contador+=1;
        print(f' La cantidad de palabras que terminan en vocales son {contador}');
        time.sleep(1);
        menu();
        opcion=(input("Ingrese 'a','b','c','d' de acuerdo a lo que desee realizar: ")).lower();
    elif opcion=='c':
        par=0;
        impar=0;
        print(f'\nc) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares');
        serie=int(input("Ingrese numeros o cero para terminar: "));
        while serie!=0:
            if serie%2==0:
                par+=1;
            else:
                impar+=1;
            print(f'\nc) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares');
            serie=int(input("Ingrese numeros o cero para terminar: "));
        if par>impar:
            print(f'Hay mayor cantidad de numeros pares');
        elif impar>par:
            print(f'Hay mayor cantidad de numeros impares');
        else:
            print(f'Hay igual cantidad de numeros pares como de impares');
        time.sleep(1);
        menu();
        opcion=(input("Ingrese 'a','b','c','d' de acuerdo a lo que desee realizar: ")).lower();        
    elif opcion=='d':
        print("Usted ha salido del programa");
        

