"""
6. Mostrar por pantalla el promedio de los números ingresados por teclado.
Se deja de pedir que el usuario agregue números una vez ingrese 0 (cero).
"""
import time;
num="";
promedio=0;
sumatoria=0;
contador=0;
while num!=0:
    num=float(input("Ingrese numero: "));
    contador+=1;
    if num==0:
        contador-=1;
    sumatoria+=num;
    promedio=sumatoria/contador;
print(f'El promedio de los numeros ingresados es de {promedio}');




