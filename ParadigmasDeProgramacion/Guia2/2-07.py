"""
7.Complejo de cines Desarrollar un programa que permita procesar funciones de un complejo
de cines. Por cada función se conoce:cantidad de espectadores y descuento(S/N).
La carga termina cuando la cantidad de espectadores sea igual a 0(cero).El programa deberá:
Calcular la recaudación total del complejo,considerando que el valor de la entrada es de $50
en los días con descuento y $75 en los días sin descuento.Determinar cuántas funciones
con descuentos efectuaron y qué porcentaje representan sobre el total de funciones
"""
import time;
print("""
---Lunes,Miercoles,Viernes con descuento
---Martes,Jueves y Sabados sin descuento
""");
time.sleep(1);
terminar="no";
aforo=int(input("\nIngrese capacidad del cine: "));
recaudacion=0;
dias_descuento=0;
dias_sin_descuento=0;
total_dias=0;
while aforo>0 and terminar=="no":
    entradas=int(input("Ingrese cantidad de entradas a comprar: "));
    time.sleep(1);
    if entradas<=aforo and aforo!=0:
        dia=(input("Ingrese dia de la funcion: ")).lower();
        print(f'\nHay disponibilidad, puede comprar {entradas} entradas.');
        aforo-=entradas;
        if dia=="lunes" or dia=="miercoles" or dia=="viernes":
            precio=50;
            print(f'Cada entrada cuesta $50 por ser un dia con descuento.\nTotal a pagar ${precio*entradas}');
            recaudacion+=(precio*entradas);
            dias_descuento+=1;
            total_dias+=1;
        else:
            precio=75;
            print(f'Cada entrada cuesta $75 sin descuento.\nTotal a pagar ${precio*entradas}');
            recaudacion+=(precio*entradas);
            dias_sin_descuento+=1;
            total_dias+=1;
print(f'La recaudacion total de la funcio es de ${recaudacion}');
print(f'Se efectuaron {dias_descuento} funciones con descuento');
print(f'Se efectuaron {dias_sin_descuento} funciones sin descuento');


