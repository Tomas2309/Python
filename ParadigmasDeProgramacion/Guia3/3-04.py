"""4. Secuencia numérica
Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar 
a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia 
b) Determinar la cantidad de números que son el cuadrado del número anterior 
c) Determinar la posición del mayor elemento impar de la secuencia """
import time;
cuadrado=0;
div_tres=0;
posicion=0;
contador=0;
num=int(input("Ingrese numeros o 0 para terminar: "));
while num!=0:
    if num%2!=0:
        if contador==0:
            ant=num;
        contador+=1;
        if num>ant:
            ant=num;
            num_mayor=posicion;
    if posicion>0:
        if (num)==anterior:
            cuadrado+=1;
            anterior=num**2;
    posicion+=1;
    if num%3==0:
        div_tres+=1;
    anterior=num**2;
    num=int(input("Ingrese numeros o 0 para terminar: "));
time.sleep(1);
print(f'La cantidad de numeros divisibles por 3 sobre el total de numeros ingresados en la secuencia es {div_tres}');
print(f'La cantidad de números que son el cuadrado del número anterior es {cuadrado}');
print(num_mayor+1);
