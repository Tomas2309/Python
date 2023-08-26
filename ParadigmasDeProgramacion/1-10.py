#10. Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.
dolar_actual=float(input('Ingrese el valor en pesos del dolar: '));
respuesta=0;
while respuesta!=1 and respuesta!=2:
    respuesta=int(input("Conversor de pesos a dolares escriba '1', Conversor de dolares en pesos escriba '2': "));
if respuesta==1:
    print("\nConversor de pesos a dolares\n");
    cant_pesos=float(input("Ingrese monto en pesos a convertir: "));
    dolares=cant_pesos/dolar_actual;
    print(f'${cant_pesos} equivalen a usd{dolares}');
else:
    print("\nConversor de dolares a pesos\n");
    cant_dolares=float(input("Ingrese monto en dolares a convertir: "));
    pesos=cant_dolares*dolar_actual;
    print(f'usd{cant_dolares} equivalen a ${pesos}');   
