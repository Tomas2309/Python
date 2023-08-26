###5. Conversión de medidas Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: yardas pulgadas cenơmetros metros Sabiendo que: 1 pie = 12 pulgadas 1 yarda = 3 pies 1 pulgada = 2.54 centímetros 1 metro =1000###

pies=float(input("Ingrese medida en pies: "));
yardas=pies/3;
pulgadas=pies*12;
centimetros=pulgadas*2.54;
metros=centimetros/100;
print(f'Los {pies} pies equivalen a {yardas} yardas');
print(f'Los {pies} pies equivalen a {pulgadas} pulgadas');
print(f'Los {pies} pies equivalen a {centimetros} centimetros');
print(f'Los {pies} pies equivalen a {metros} metros')