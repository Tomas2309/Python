"""
9. Promedio de números aleatorios: Realice un programa que permita calcular el promedio
de 1000 números aleatorios generados en el rango de[0,100000]
"""
import time;
import random;
sumatoria=0;
contador=0;
for i in range(0,1000):
    numeros=random.randint(0,100000);
    sumatoria+=numeros;
    contador+=1;
print(f'El promedio de 1000 num aleatorios es de {sumatoria/contador}');

