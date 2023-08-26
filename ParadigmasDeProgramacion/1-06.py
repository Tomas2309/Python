###6. Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar.###

nombre=input("Ingrese nombre de usuario: ");
cantLetras=len(nombre);
if (cantLetras%2)==0:
    print(f'La cantidad de letras de "{nombre}" es PAR porque tiene {cantLetras} letras.');
else:
    print(f'La cantidad de letras de "{nombre}" es IMPAR porque tiene {cantLetras} letras.');