###4 - Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero? ¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado, y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado) ###
print("El ultimo digito");
numEnt=int(input("Ingrese un numero entero: "));
digito=numEnt%10;
print(f'El ultimo digito es {digito}');
print("/nDos ultimos digitos");
digitos=numEnt%100;
print(f'Los dos ultimos digitos son {digitos}');
