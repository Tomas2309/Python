"""
8. Ventas por sucursal Ingresar una serie de números por teclado que representan la cantidad
de ventas realizadas en las diferentes sucursales de un país de una determinada empresa.
Los requerimientos del programa son: Informar la cantidad de ventas ingresadas
Total de ventas .Cant de ventas cuyo valores te comprendido entre 100 y 300 unidades
Candad de ventas con 400,500y600 unidades.Indicar si hubo una cantidad de ventas inferior
a 50 unidades. Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor
negativo

"""
import time;
cantidad=0;
sumatoria=0;
rango=0;
rango_min=0;
unidades=0;
while cantidad>=0:
    cantidad=int(input("Ingrese cantidad de ventas: "));
    if cantidad>=0:
        sumatoria+=cantidad;
    if cantidad>=100 and cantidad<=300:
        rango+=1;
    elif cantidad==400 or cantidad==500 or cantidad==600:
        unidades+=1;
    elif cantidad<=50 and cantidad>=0:
        rango_min+=1;
print(f'La cantidad de ventas totales es de {sumatoria} ventas');
print(f'La cant de ventas entre 100 y 300 unidades son {rango}');
print(f'La cant de ventas con 400, 500 y 600 unidades son {unidades}');
print(f'La cant de ventas menores a 50 unidades son {rango_min}');

