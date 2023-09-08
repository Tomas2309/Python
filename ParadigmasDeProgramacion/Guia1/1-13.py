#13. Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas: Componer la dirección de correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar la dirección de mail sería: fsteffolani@umet.edu.ar. Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar: .@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:
#soledad.steffolani@colegiorosarito.edu.ar

nombre=input("Ingrese su nombre: ");
apellido=input("Ingrese su apellido: ");
dominio=input("Ingrese Dominio: ");
name_caracter=nombre[0].lower();
surname_caracter=apellido[0].lower();
apellido=apellido.lower();
if (name_caracter==surname_caracter):
    mail=name_caracter+"."+apellido+"@"+dominio;
else:
    mail=name_caracter+apellido+"@"+dominio;
print(f'El mail generado es {mail}');
