"""
5.Analisis de Texto
El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero. La frase finaliza con
un punto, y las palabras están separadas por espacios únicamente.
Se debe mostrar:
a) Ver el porcentaje de vocales respecto del total de letras de la frase.
b) La longitud promedio de las palabras
c) La longitud de la palabra mas larga del texto
d) Cantidad de palabras que comienzan con "ta"
"""
import time;
frase=str("");
lista=[];
larga=0;
contador=0;
sumatoria=0;
vocales=0;
ta=0;
while frase=="":
    frase=input("Ingrese una frase que termine con un punto: ");
    time.sleep(1);
frase=frase.replace(".","");
lista.append(frase.split());
frase=frase.replace(" ","");
letras_total=len(frase);
for letra in frase:
    if letra in 'aeiou':
        vocales+=1;
porcentaje_v=(vocales*100)/letras_total;
print(f'El porcentaje de vocales es de {porcentaje_v}%');
for i in range(0,len(lista[0])):
    contador+=1;
    sumatoria+=len(lista[0][i]);
    if len(lista[0][i])>larga:
        larga=len(lista[0][i]);
        plarga=lista[0][i];
    if lista[0][i].startswith("ta"):
        ta+=1;
print(f'Hay {contador} palabras y el promedio de letras es de {sumatoria/contador}');
print(f'La longitud de la palabra mas larga ({plarga}) es de {larga} letras');
print(f'Las palabras que empiezan con TA son {ta}');




