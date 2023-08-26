###3 - Área de un triángulo Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base. ###
base=float(input("Ingrese la medida 'base' del triangulo: "));
altura=base**2;
area=(base*altura)/2;
print(f'El area del triangulo es {area}');