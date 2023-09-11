"""
4. Decimal a Hexadecimal: Generar n números aleatorios entre el rango de 5000 y 450000,
por cada uno de ellos mostrar y generar el numero hexadecimal

"""
import time;
import random;
cantidad=int(input("Indique cuantos numeros generar: "));
for i in range(0,cantidad):
    num=random.randint(5000,450000);
    hexadecimal=(hex(num));
    print(f'El Hexadecimal de {num} es {hexadecimal}');
