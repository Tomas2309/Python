"""1. Comisión de vendedores Una empresa debe calcular el total de comisiones
que debe abonar por ventas realizadas por sus vendedores, para ello les solicita un
sistemita que le permita calcular dichos montos. Se tiene conocimiento que la
empresa tiene cuatro categorías de vendedores(1 a 4).Usted debe solicitar el
ingreso de la categoría del vendedor y el total de la venta(el proceso termina
cuando se ingrese una categoría igual a cero) y acumular las comisiones de las
ventas rendidas por los vendedores de diferentes en base a los siguientes cálculos: 
Categoría1: cobra una comisión de 10% 
Categoría2: cobra una comisión de 25% 
Categoría3: cobra una comisión de 30% 
Categoría4: cobra una comisión de 40% 
Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por
cada categoría de vendedor es que en el la empresa junto con el total general """

import time;
import math;
comision1=0;
comision2=0;
comision3=0
comision4=0;
categoria=int(input("Ingrese la categoría del vendedor o '0' para terminar: "));
while categoria<0 or categoria>4:
    print("Error, ingrese una categoria valida");
    categoria=int(input("Ingrese la categoría del vendedor o '0' para terminar: "));
while categoria>=1 and categoria<=4:
    total_ventas=int(input("Ingrese el total de ventas del vendedor: "));
    if categoria==1:
        comision1_ind=total_ventas*0.10;
        comision1+=comision1_ind;
    elif categoria==2:
        comision2_ind=total_ventas*0.25;
        comision2+=comision2_ind;
    elif categoria==3:
        comision3_ind=total_ventas*0.30;
        comision3+=comision3_ind;
    else:
        comision4_ind=total_ventas*0.40;
        comision4+=comision4_ind;
    categoria=int(input("Ingrese la categoría del vendedor o '0' para terminar: "));
    while categoria<0 or categoria>4:
        print("Error, ingrese una categoria valida");
        categoria=int(input("Ingrese la categoría del vendedor o '0' para terminar: "));
if categoria==0:
    com_total=comision1+comision2+comision3+comision4;
    print(f'La categoria 1 recibe {comision1} de comision');
    print(f'La categoria 2 recibe {comision2} de comision');
    print(f'La categoria 3 recibe {comision3} de comision');
    print(f'La categoria 4 recibe {comision4} de comision');
    print(f'La empresa paga {com_total} de comisiones');
