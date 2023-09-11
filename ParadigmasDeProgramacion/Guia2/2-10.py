"""
10.  Búsqueda de mayor Realizar un programa que permita buscar el mayor de 10.000
números aleatorios generados en el rango de[0,100.000]. 
"""
import time;
import random;
contador=0;
mayor=-1;
for i in range(0,10000):
    numeros=random.randint(0,100000);
    if numeros>mayor:
        mayor=numeros;
print(f'El mayor de 10.000 núm aleatorios entre [0,100.000] es {mayor}');

