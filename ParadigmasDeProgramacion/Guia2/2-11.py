"""
11. Menores y promedio Realizar un programa que genere 5000 numeros aleatorios en el
rango de [0,100000] y que permita:Determinar el menor de los numeros generados en forma
aleatoria. Calcular el valor promedio de los números menores a 10.000
"""
import time;
import random;
contador=0;
sumatoria=0;
menor=100001;
for i in range(0,5000):
    numeros=random.randint(0,100000);
    if numeros<menor:
        menor=numeros;
    if numeros<10000:
        contador+=1;
        sumatoria+=numeros;
print(f'El menor de 5.000 núm aleatorios entre [0,100.000] es {menor}');
print(f'El promedio de los núm aleatorios menores a 10.000 es {sumatoria/contador}');

