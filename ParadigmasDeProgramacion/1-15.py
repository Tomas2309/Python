#15.  Suma - División - Potencia Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.

num1=float(input("Ingrese primer numero: "));
num2=float(input("Ingrese segundo numero: "));
num3=float(input("Ingrese tercer numero: "));
suma=num1+num2+num3;
print(f'La suma de los numeros da igual a {suma}');
if suma>10:
    print(f'{suma/2} es el resultado de la division entre {suma} y 2');
else:
    print(f'{suma**3} es el resultado de elevar {suma} al cubo');