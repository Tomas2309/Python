#11. Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
sumatoria_ahorro=float(0);
for i in range(0,12):
    sueldo_mensual=float(input(f'Ingrese sueldo de {meses[i]}: '));
    ahorro_mensual=sueldo_mensual*0.1;
    print(f'Tu ahorro mensual del 10% en {meses[i]} es ${ahorro_mensual}')
    sumatoria_ahorro+=ahorro_mensual;
    print(f'Llevas ahorrado ${sumatoria_ahorro} este ano');
