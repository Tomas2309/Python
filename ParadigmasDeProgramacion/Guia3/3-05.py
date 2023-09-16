"""5. Proceso de discriminantes
Un matemático desea un simple programa que le permita cargar una serie de números quere presentan los discriminantes
de diferentes ecuaciones de segundo grado, el proceso de la secuencia analiza cuando el matemático no desea seguir cargando discriminantes.
Usted debe:
a) Determinar la cantidad de discriminantes quedarán 2 raíces 
b) Determinar la cantidad de discriminantes quedarán una única raíz
c) Determinar la cantidad de discriminantes quedaran raíces en el campo de los números imaginarios
d) Indicar el porcentaje que representa el punto c sobre el total de discriminantes procesados por el matemático
"""
import math;
import time;
opcion=1;
total=0;
imaginario=0;
rmulti=0;
runica=0;
while opcion==1:
    print("\nEcuaciones de 2do grado del tipo Ax2 + Bx + C\n");
    a=float(input("Ingrese valor A: "));
    b=float(input("Ingrese valor B: "));
    c=float(input("Ingrese valor C: "));
    total+=1
    try:
        disc=math.sqrt((b**2)-4*a*c);
        print(f'El resultado del discriminante es: {disc}');
        if disc==0:
            rmulti+=1;
        elif disc>0:
            runica+=1;
    except ValueError:
        print("Resultado no valido para los numeros reales");
        imaginario+=1;
    time.sleep(1);
    opcion=int(input("Si desea ingresar otra ecuacion escriba '1', sino escriba '0': "));
print(f'\nLa cantidad de discriminantes en los que quedarán 2 raíces son {rmulti}');
print(f'La cantidad de discriminantes en los que quedará 1 raíz son {runica}');
print(f'La cantidad de discriminantes en los que quedaran raíces imaginarias son {rmulti}');
print(f'El porcentaje que representa el punto c sobre el total de discriminantes procesados por el matemático es {(imaginario*100)/total}');
