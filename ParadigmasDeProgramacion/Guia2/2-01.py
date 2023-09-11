"""1. Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
Hace un programa que cargue, por cada competidor, nombre y time de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera.
Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas """
import time;
import math;
lista_competidores=[];
promedio_s=int(0);
promedio_m=int(0);
promedio_hs=int(0);
contador=0;
ganadores=1;
n_ciclistas=int(input("\nIngrese la cantidad de competidores de la carrera: "));
time.sleep(1);
while n_ciclistas <=0:
    print("Ingrese una cantidad valida, pruebe otra vez...");
    time.sleep(0.5);
    n_ciclistas=int(input("Ingrese la cantidad de competidores de la carrera: "));
    time.sleep(1);
for i in range (0,n_ciclistas):
    tiempo=[];
    competidor=input(f'\nIngrese nombre del competidor "{i+1}": ');
    print(f'\nIngrese el tiempo del competidor "{i+1}"');
    time_hs=int(input("Ingrese horas: "));
    time_m=int(input("Ingrese minutos: "));
    time_s=int(input("Ingrese segundos: "));
    print(f'Tiempo ingresado para {competidor}: {time_hs} hs, {time_m} min, {time_s} seg');
    time.sleep(1);
    option=int(input("Son correctos los datos ingresados? '1' para SI, '2' para NO: "));
    while option!=1:
        competidor=input(f'\nIngrese nombre del competidor "{i+1}": ');
        print(f'\nIngrese el tiempo del competidor "{i+1}');
        time_hs=int(input("Ingrese horas: "));
        time_m=int(input("Ingrese minutos: "));
        time_s=int(input("Ingrese segundos: "));
        print(f'\nTiempo ingresado para {competidor}: {time_hs} hs, {time_m} min, {time_s} seg\n');
        time.sleep(1);
        option=int(input("Son correctos los datos ingresados? '1' para SI, '2' para NO: "));
    tiempo.append(competidor);
    tiempo.append(time_hs);
    tiempo.append(time_m);
    tiempo.append(time_s);
    lista_competidores.append(tiempo);
    contador+=1;
    if contador==1:
          best_time=tiempo;
    else:
        if tiempo[1]<=best_time[1]:
            if tiempo[1]<best_time[1]:
                best_time=tiempo;
            else:
                if tiempo[2]<=best_time[2]:
                    if tiempo[2]<best_time[2]:
                        best_time=tiempo;
                    else:
                        if tiempo[3]<=best_time[3]:
                            if tiempo[3]<best_time[3]:
                                best_time=tiempo;
                            else:
                                ganadores+=1;
                                best_time.append(competidor);
if ganadores>1:
    print(f'Los ganadores son: {best_time[0]},',end=' ');
    for j in range(4,3+ganadores):
        print(f', {best_time[j]}',end=' ');
else:
    print(f'El ganador es {best_time[0]}');
time.sleep(1.5);
print(f'\nIngrese el tiempo Record:');
record_hs=int(input("Ingrese horas: "));
record_m=int(input("Ingrese minutos: "));
record_s=int(input("Ingrese segundos: "));
print(f'El tiempo record ingresado es: {record_hs} hs, {record_m} min, {record_s} seg');
time.sleep(1);
option2=int(input("Son correctos los datos ingresados? '1' para SI, '2' para NO: "));
print();
time.sleep(1);
while option2!=1:
    print(f'\nIngrese el tiempo Record:');
    record_hs=int(input("Ingrese horas: "));
    record_m=int(input("Ingrese minutos: "));
    record_s=int(input("Ingrese segundos: "));
    print(f'El tiempo record ingresado es: {record_hs} hs, {record_m} min, {record_s} seg');
    time.sleep(1);
    option2=int(input("Son correctos los datos ingresados? '1' para SI, '2' para NO: "));
if best_time[1]<=record_hs:
    if best_time[1]<record_hs:
        print("El tiempo del ganador es menor al tiempo record y se transforma en el mejor tiempo");
    else:
        if best_time[2]<=record_m:
            if best_time[2]<record_m:
                print("El tiempo del ganador es menor al tiempo record y se transforma en el mejor tiempo");
            else:
                if best_time[3]<=record_m:
                    if best_time[2]<record_m:
                        print("El tiempo del ganador es menor al tiempo record y se transforma en el mejor tiempo");
                    else:
                        print("Ambos tiempos son iguales. El tiempo actual iguala al Record");
else:
    time.sleep(1);
    print("El tiempo del ganador es mayor al tiempo record\n");
for x in range(0,n_ciclistas):
    promedio_s+=lista_competidores[x][3];
    promedio_m+=lista_competidores[x][2];
    promedio_hs+=lista_competidores[x][1];
promedio_hs=promedio_hs/n_ciclistas;
if promedio_hs<1 and promedio_hs>0:
    decimales=promedio_hs*60;
    promedio_m+=decimales;
    promedio_hs=math.floor(promedio_hs);
promedio_m=promedio_m/n_ciclistas;
if promedio_m<1 and promedio_m>0:
    decimales=promedio_m*60;
    promedio_s+=decimales;
    promedio_m=math.floor(promedio_m);
promedio_s=promedio_s/n_ciclistas;
promedio_s=round(promedio_s,1);
promedio_m=round(promedio_m,1);
promedio_hs=round(promedio_hs,1);
time.sleep(1);
print(f'El tiempo promedio entre todos es {promedio_hs} horas, {promedio_m} minutos y {promedio_s} segundos');
