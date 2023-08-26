#9. Escribir un programa que pida dos números y muestre como resultado su división, cociente y resto.
num1=float(input("Ingrese un numero: "));
num2=float(input("Ingrese otro numero: "));
print(f'La division da como resultado {num1/num2}');
print(f'La division da como cociente {num1//num2}');
print(f'La division da como resto {num1%num2}');