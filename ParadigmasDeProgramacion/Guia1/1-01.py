###1 - División con resto Plantear un algoritmo que permita informar, para dos valores a y b el resultado de la división a/b y el resto de esa división.###
valorA=float(input("Ingrese un primer valor: "));
valorB=float(input("Ingrese un segundo valor: "));
resultadoDiv=valorA/valorB;
restoDiv=valorA%valorB;
print(f'La division entre {valorA} y {valorB} da como resultado: {resultadoDiv}');
print(f'El resto de la division entre {valorA} y {valorB} da como resultado: {restoDiv}');