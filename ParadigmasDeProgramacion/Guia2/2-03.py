"""
3. Sueldos y aguinaldo
Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
b) Determinar en qué mes recibió el sueldo más bajo del período.
c) Informar el sueldo promedio del semestre.

"""
import time;
suma_sueldo=0;
contador=0;
mayor=float();
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio"];
for i in range(0,len(meses)):
    contador+=1;
    sueldo=float(input(f'Ingrese el sueldo de {meses[i]}: '));
    if contador==1:
        mes_menor=meses[i];
        menor=sueldo;
    else:
        if sueldo<menor:
            menor=sueldo;
            mes_menor=meses[i]
    if sueldo>mayor:
        mayor=sueldo;
    suma_sueldo+=sueldo;    
aguinaldo=mayor/2;
print(f'El aguinaldo es de ${aguinaldo}');
print(f'En {mes_menor} se recibio el sueldo mas bajo');
print(f'El sueldo promedio es {suma_sueldo/6}');
