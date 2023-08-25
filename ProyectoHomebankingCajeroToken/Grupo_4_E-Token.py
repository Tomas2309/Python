                                    #E TOKEN
#Variables
import time;
import random;
opcion_codigo=int();
contra_dsd=int(12345);#Contrasena de seguridad digital 12345
contra_ingresada=int();
intento=int(3);
pin_acceso=str(); #Codigo de acceso
numero=int();
codigo_acceso=[];
codigo_reaut=[];
codigo_transaccion=[];
numero_r=int();
pin_reaut=str();#Codigo de reautenticacion
digitos_ob=str();#Digitos solicitados en Online Banking (ultimos 4 digitos del CBU)
numero_t=int();
pin_transaccion=str();#Codigo de transaccion
bloqueada=str();

#txt-cbu-ultimos-4-digitos
with open ("cbutxt.txt") as archivo1:
    for linea in archivo1:
        linea=linea.replace("'","");
        digitos_ob=linea;
#Funciones
def menu_codigo():
    print("\n\t\tDISPOSITIVO DE SEGURIDAD DIGITAL\n");
    print("""Selecciona el codigo de seguridad que necesitas:
    1:  Codigo de Seguridad de Transaccion
    2:  Codigo de Seguridad de Acceso
    3:  Codigo de Seguridad de Reautenticacion
    4:  Salir

    """);
#Algoritmos
menu_codigo();
opcion_codigo=int(input("Escriba la opcion a realizar: "));
while opcion_codigo!=4:
    while (opcion_codigo<1 or opcion_codigo>3)and opcion_codigo!=4 and bloqueada!="si":
        time.sleep(1);
        print("\nError!, ingrese una opcion valida\n");
        time.sleep(1.5);
        menu_codigo();
        opcion_codigo=int(input("Escriba la opcion a realizar: "));
        
    if opcion_codigo==1 and bloqueada!="si": #de transaccion
        time.sleep(1);
        intento=int(3);
        print("\nHas seleccionado el Codigo de Seguridad de Transaccion...\n");
        digitos_ob_entrada=str(input("Ingresa los digitos solicitados en Online Banking: "));
        contra_ingresada=int(input("Ingrese la contrasena de seguridad del dispositivo: "));
        while (digitos_ob_entrada!=digitos_ob or contra_ingresada!=contra_dsd) and intento<=3 and intento>=1:
            intento-=1;
            print(f'\nDigito o Contrasena invalido, le quedan {intento} intentos\n');
            time.sleep(1);
            if intento>=1:
                digitos_ob_entrada=str(input("Ingresa los digitos solicitados en Online Banking: "));
                contra_ingresada=int(input("Ingrese la contrasena de seguridad del dispositivo: "));
        if intento>=1:
            print("\nContrasena y Digito Correcto, Generando Codigo de Seguridad de Transaccion...");
            time.sleep(1);
            for i in range(4,0,-1):
                print(f'Espere {i} segundos...');
                time.sleep(1);
            print("\nCodigo generado");
            for k in range (0,6):
                numero_t=random.randrange(10);
                codigo_transaccion.append(numero_t);
                pin_transaccion+=str(codigo_transaccion[k]);
            pin_transaccion=int(pin_transaccion)
            print(f'El Codigo de Seguridad de Transaccion es: {pin_transaccion}');
            archivo=open("CodigoTransaccion.txt","w");
            string3=repr(pin_transaccion)
            archivo.write(string3);
            archivo.close();
            time.sleep(1);
            menu_codigo();
            time.sleep(0.3);
            opcion_codigo=int(input("Escriba la opcion a realizar: "));
            pin_transaccion="";
            codigo_transaccion=[];
        else:
            print("Cuenta Bloqueada");
            bloqueada="si";
        
    if opcion_codigo==2 and bloqueada!="si": #de acceso
        intento=int(3);
        time.sleep(1);
        print("\nHas seleccionado el Codigo de Seguridad de Acceso...\n");
        contra_ingresada=int(input("Ingrese la contrasena de seguridad del dispositivo: "));
        while contra_dsd!=contra_ingresada and intento<=3 and intento>=1:
            intento-=1;
            print(f'\nContrasena incorrecta, le quedan {intento} intentos\n');
            time.sleep(1);
            if intento>=1:
                contra_ingresada=int(input("Ingrese la contrasena de seguridad del dispositivo: "));
        if intento>=1:
            print("\nContrasena Correcta, Generando Codigo de Acceso...");
            time.sleep(1);
            for i in range(4,0,-1):
                print(f'Espere {i} segundos...');
                time.sleep(1);
            print("\nCodigo generado");
            for j in range (0,6):
                numero=random.randrange(10);
                codigo_acceso.append(numero);
                pin_acceso+=str(codigo_acceso[j]);
            pin_acceso=int(pin_acceso)
            print(f'El Codigo de Acceso es: {pin_acceso}');
            archivo=open("CodigoAcceso.txt","w");
            string=repr(pin_acceso)
            archivo.write(string);
            archivo.close();
            time.sleep(1);
            menu_codigo();
            time.sleep(0.3);
            opcion_codigo=int(input("Escriba la opcion a realizar: "));
            pin_acceso="";
            codigo_acceso=[];
        else:
            print("Cuenta Bloqueada");
            bloqueada="si";

    if opcion_codigo==3 and bloqueada!="si": #de reutenticacion
        intento=int(3);
        time.sleep(1);
        print("\nHas seleccionado el Codigo de Seguridad de Reutenticacion...\n");
        contra_ingresada=int(input("Ingrese la contrasena de seguridad del dispositivo: "));
        while contra_dsd!=contra_ingresada and intento<=3 and intento>=1:
            intento-=1;
            print(f'\nContrasena incorrecta, le quedan {intento} intentos\n');
            time.sleep(1);
            if intento>=1:
                contra_ingresada=int(input("Ingrese la contrasena de seguridad del dispositivo: "));
        if intento>=1:
            print("\nContrasena Correcta, Generando Codigo de Reutenticacion...");
            time.sleep(1);
            for i in range(4,0,-1):
                print(f'Espere {i} segundos...');
                time.sleep(1);
            print("\nCodigo generado");
            for t in range (0,6):
                numero_r=random.randrange(10);
                codigo_reaut.append(numero_r);
                pin_reaut+=str(codigo_reaut[t]);
            pin_reaut=int(pin_reaut)
            print(f'El Codigo de Reutenticacion es: {pin_reaut}');
            archivo=open("CodigoReautenticacion.txt","w");
            string2=repr(pin_reaut)
            archivo.write(string2);
            archivo.close();        
            time.sleep(1);
            menu_codigo();
            time.sleep(0.3);
            opcion_codigo=int(input("Escriba la opcion a realizar: "));
            pin_reaut="";
            codigo_reaut=[];
        else:
            print("Cuenta Bloqueada");
            bloqueada="si";
time.sleep(1);
print("\nHa salido del programa, hasta la proxima");
