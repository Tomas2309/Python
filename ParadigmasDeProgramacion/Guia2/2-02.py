"""2. Secuencia de impares: Cargar por teclado dos números, e imprimir los números impares
    que se encuentran comprendidos entre ellos, en forma ascendente y descendente
"""
import time;
num1=int(input("Ingrese un numero: "));
num2=int(input("Ingrese otro numero: "));
time.sleep(1);
if num2!=num1:
    if num2>num1:
        mayor=num2;
        menor=num1;
    else:
        mayor=num1;
        menor=num2;
    print("Forma ascendente: ");
    time.sleep(1);
    for i in range(menor+1,mayor):
        print(i,end=" ");
    print("\nForma Descendente: ");
    time.sleep(1);
    for j in range(mayor-1,menor,-1):
        print(j,end=" ");
else:
    print("Los numero son iguales");
