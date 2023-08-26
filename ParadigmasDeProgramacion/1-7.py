#7. Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.

cantidad=int(input("Ingrese una cantidad: "));
anterior=int(0);
actual=int(1);
contador=int(0);
for i in range(0,cantidad):
    contador+=1;
    if (contador<=2):
        print(i);
    else:
        siguiente=anterior+actual;
        print(siguiente);
        anterior=actual;
        actual=siguiente;
