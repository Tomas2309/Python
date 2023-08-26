#8. Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.
numero=float(input("Ingrese un numero: "));
for i in range (1,11):
    print(f'{numero} X {i} = {numero*i}');