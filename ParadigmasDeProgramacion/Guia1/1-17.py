#17. Galería de Arte Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000). Determinar cuántos tienen antigüedad inferior a 10 años. Si no hay ninguno, imprimir el mensaje “Renovar stock”.
contador=0;
contador2=0;
for i in range(0,3):
    ano=int(input("Ingrese año del cuadro:"));
    if ano<1901:
        contador+=1;
    elif ano>=2014:
        contador2+=1;
if contador==3:
    print("Todos los cuadros son anteriores al siglo XX");
elif contador!=3:
    print("No todos los cuadros son anteriores al siglo XX");
    print(f'Hay {contador2} cuadros con menos de 10 años de antiguedad');
else:
    print("Renovar Stock");