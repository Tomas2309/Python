"""19.Elecciones presidenciales 
Según la Ley Electoral de la República ArgenƟna, el Presidente y el Vicepresidente se eligen de acuerdo a las siguientes reglas: 
Articulo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %) de los votos afirmaƟvos válidamente emitidos; en su defecto, aquella que hubiere obtenido el cuarenta por ciento (40 %) por lo menos de los votos afirmaƟvos válidamente emiƟdos y, además, existiere una diferencia mayor de diez puntos porcentuales respecto del total de los votos afirmaƟvos válidamente emitidos sobre la fórmula que le sigue en número de votos. 
Arơculo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escrutnio ejecutado por las Juntas Electorales, y cuyo resultado único para toda la Nación será anunciado por la Asamblea Legislatva atento lo dispuesto por el arơculo 120 de la presente ley, se realizará una segunda vuelta dentro de los treinta (30) días. 
Articulo 151. — En la segunda vuelta parƟciparán solamente las dos fórmulas más votadas en la primera, resultando electa la que obtenga mayor número de votos afirmaƟvos válidamente emiƟdos. Desarrollar un programa que permita ingresar, para los 3 parados más votados: fórmula (presidente + vice) y cantidad de votos obtenidos. Luego determinar: Qué fórmula obtuvo el mayor porcentaje. Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso, indicar también quienes parƟcipan de la segunda vuelta"""

print("\nPartido 1:\n");
presidente1=input("Ingrese el apellido del candidato a presidente 1: ");
vice1=input("Ingrese el apellido del candidato a vicepresidente 1: ");
votos1=float(input("Ingrese votos obtenidos: "));
print("\nPartido 2:\n");
presidente2=input("Ingrese el apellido del candidato a presidente 2: ");
vice2=input("Ingrese el apellido del candidato a vicepresidente 2: ");
votos2=float(input("Ingrese votos obtenidos: "));
print("\nPartido 3:\n");
presidente3=input("Ingrese el apellido del candidato a presidente 3: ");
vice3=input("Ingrese el apellido del candidato a vicepresidente 3: ");
votos3=float(input("Ingrese votos obtenidos: "));

votos_totales=votos1+votos2+votos3;

#partido1,2 y 3
porcentaje_votos1=(votos1*100)/votos_totales;
porcentaje_votos2=(votos2*100)/votos_totales;
porcentaje_votos3=(votos3*100)/votos_totales;
if porcentaje_votos1>porcentaje_votos2:
    porcentaje1=porcentaje_votos1;
    mayor_porcentaje="Partido 1: "+presidente1+" "+vice1;
    if porcentaje_votos2>porcentaje_votos3:
        segundo_porcentaje="Partido 2: "+presidente2+" "+vice2;
        porcentaje2=porcentaje_votos2;
    else:
        segundo_porcentaje="Partido 3: "+presidente3+" "+vice3;
        porcentaje2=porcentaje_votos3;
elif porcentaje_votos2>porcentaje_votos1:
    porcentaje1=porcentaje_votos2;
    mayor_porcentaje="Partido 2: "+presidente2+" "+vice2;
    if porcentaje_votos1>porcentaje_votos3:
        segundo_porcentaje="Partido 1: "+presidente1+" "+vice1;
        porcentaje2=porcentaje_votos1;
    else:
        segundo_porcentaje="Partido 3: "+presidente3+" "+vice3;
        porcentaje2=porcentaje_votos3;
else:
    porcentaje1=porcentaje_votos3;
    mayor_porcentaje="Partido 3: "+presidente3+" "+vice3;
    if porcentaje_votos1>porcentaje_votos2:
        segundo_porcentaje="Partido 1: "+presidente1+" "+vice1;
        porcentaje2=porcentaje_votos1;
    else:
        segundo_porcentaje="Partido 2: "+presidente2+" "+vice2;
        porcentaje2=porcentaje_votos2;
print();
print(f'La formula que obtuvo el mayor porcentaje es la del: {mayor_porcentaje} con el {porcentaje1}% de los votos\n');
print(f'La formula que quedo segunda es la del: {segundo_porcentaje} con el {porcentaje2}% de los votos\n');
if (porcentaje1>=45) or (porcentaje1>=40 and porcentaje2<=30):
    print(f'La fórmula del {mayor_porcentaje} resulta elegida');
else:
    print(f'Hay segunda vuelta entre el {mayor_porcentaje} y el {segundo_porcentaje}');