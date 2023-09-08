###2 - Cuadrado de un binomio Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) esigual al cuadrado del primer término, más el doble producto del primero por el segundo más el cuadrado del segundo. ###
valorA=float(input("Ingrese primer valor: "));
valorB=float(input("Ingrese segundo valor: "));
binomio=(valorA+valorB)**2;
formula=valorA**2+2*valorA*valorB+valorB**2;
print(f'La resolucion del binomio da como resultado {binomio} y La resolucion de la formula da como resultado {formula}');