"""
13. Desarrollar un programa que permita procesar los datos del último censo de una pequeña
población.Por cada habitantes e ingresa:sexo(M/F)y edad. La carga de datos analiza al
ingresar cualquier otro valor para sexo. El programa debe informar: Aqué sexo corresponde la
mayor cantidad de habitantes(considerar que puede ser igual) Cantidad de mujeres en edad
escolar(4 a 18 años inclusive)Si hay algún varón que supere los 80 años de edad"""
import time;
opcion=1;
hombre=0;
mujer=0;
escolar=0;
grande=0;
while opcion==1:
    sexo=int(input("\nIngrese el sexo (1 para hombre,2 para mujer): "))
    if sexo==1:
        hombre+=1;
        edad=int(input("Ingrese la edad: "));
        if edad>80:
            grande+=1;
    elif sexo==2:
        mujer+=1;
        edad=int(input("Ingrese la edad: "));
        if edad>=4 and edad<=18:
            escolar+=1;
    opcion=int(input("\nIngresa 1 para continuar la carga de datos, o 0 para terminar: "));
if hombre>mujer:
    print("Hay mas hombres que mujeres");
elif mujeres>hombres:
    print("Hay mas mujeres que hombres");
else:
    print("Hay igual cantidad de mujeres que hombres");
print(f'Hay {escolar} mujeres en edad escolar.')
print(f'Hay {grande} hombres mayores de 80.')
    

