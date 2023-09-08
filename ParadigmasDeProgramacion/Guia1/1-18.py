#18. Tarjeta de Bingo Realizar un programa que genere 15 numero aleatorios enteros en el rango del 1 al 100, que representaria la tarjeta de bingo de una persona. Una vez generado los numeros aleatorios solicitar al usuario que ingrese 3 numeros enteros, a parƟr de alli mostrar los siguientes mensajes: Si el usuario no marco ninguno de los numeros indicarlo diciendo “El jugador Ɵene mala suerte, no marco ninguna casilla”. Caso contrario mostrar “El jugador marco algun numero de la tarjeta”. 
import random;
coincidir="no";
lista_num=[];
for i in range(0,15):
    num=random.randrange(1,101);
    lista_num.append(num);
print (lista_num);
print("Ingrese tres numeros enteros");
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
num3=int(input("Ingrese otro numero: "))
for j in range(0,15):
    if num1==lista_num[j] or num2==lista_num[j] or num3==lista_num[j]:
        coincidir="si";
if coincidir=="no":
    print("El jugador tiene mala suerte, no marco ninguna casilla");
else:
    print("El jugador marco algun numero de la tarjeta")