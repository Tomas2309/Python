"""
12. Números pares e impares Se pide desarrollar un programa que permita leer una serie
de números . La finalización de carga de datos se presenta cuando el usuario ingrese un
número negativo. Los requerimientos funcionales del programa son:La sumatoria de solo
los números que estén comprendidos entre 50y100. Cantidad de valores pares ingresados.
Cantidad de valores impares ingresados. Informar si en la carga de números se ingreso
al menos un número 0. """
import time;
num=int();
sumatoria=0;
pares=0;
impares=0;
cero=0;
while num>=0:
    num=int(input("Ingrese un numero: "));
    if num>=50 and num<=100:
        sumatoria+=num;
    if num>=0:
        if num%2==0:
            pares+=1;
        if num%2!=0:
            impares+=1;
        if num==0:
            cero+=1;
print(f'La sumatoria de los números que estén comprendidos entre 50y100 es {sumatoria}');
print(f'La Cantidad de valores pares ingresados es de {pares}');
print(f'La Cantidad de valores impares ingresados es de {impares}');
print(f'Se ingresaron {cero} cantidad de ceros');
