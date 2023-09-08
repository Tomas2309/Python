#12. Crear un conversor de pies y pulgadas a centímetros.
print("\nConversor de pies y pulgadas\n");
print("""
1) Convertir pies a centimetros
2) Convertir pulgadas a centimetros
""");
opcion=int(input("Ingrese 1 o 2 dependiendo del conversor a utilizar: "));
print();
while opcion!=1 and opcion!=2:
    opcion=int(input("Ingrese 1 o 2 dependiendo del conversor a utilizar: "));
if opcion==1:
    pies=float(input("Ingrese valor en pies: "));
    print(f'{pies} pies equivalen a {pies*30.48} centimetros')
else:
    pulgadas=float(input("Ingrese valor en pulgadas: "));
    print(f'{pulgadas} pulgadas equivalen a {pulgadas*2.54} centimetros')
