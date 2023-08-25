                                            #CAJERO AUTOMATICO

#declaracion-variables
iniciar=int();
option1=int();
usuarios_registrados=["tomasaguirre","tomasperalta","nahuelcano","adrianafachal"];
contrasena_registrados=["1234","4231","2606","0000"];
usuario=str();
contrasena=str();
perfil=str("");
error=str("");
intentos=int(3);
saldo_actual=int(500);
monto_deposito=int();
monto_retiro=int();
pin_anterior=str();
pin=str("");
pin_usuario=str();
volver=str("si");
#menu
def menu_principal():
    print("""------------------------
    \tMENU
    1: Consultar Saldo
    2: Depositar
    3: Retirar
    4: Cambiar PIN
    5: Salir
    ------------------------
    """);
def menu_cantidades():
    print("""------------------------
    \tMENU
    1: 50
    2: 100
    3: 200
    4: 500
    5: Salir
    ------------------------
    """);
#algoritmos
import time;
print("\n\t\t******************************************************************");
print("\t\t -   BIENVENIDOS  AL BANCO UNIDO DEL GRUPO 4  -");
print("\t\t********************************************************************");
time.sleep(1);
iniciar=int(input("Escriba '1' para iniciar: "));
while (iniciar!=1):
    iniciar=int(input("\nEscriba '1' para iniciar: "));
time.sleep(1.5)
while volver=="si":
    print("\n\t\t-------------------------------------------------------------------------------");
    print("\t\t|                                           LOG IN                                |");
    print("\t\t-------------------------------------------------------------------------------\n");
    time.sleep(1)
    while error=="" and intentos>=1:
        usuario=str(input("Ingrese Usuario: "));
        usuario=usuario.lower().replace(" ","");
        contrasena=str(input("Ingrese Contrasena: "));
        for i in range(0,len(usuarios_registrados)):
            if usuario==usuarios_registrados[i] and contrasena==contrasena_registrados[i]:
                pin_usuario=contrasena_registrados[i]
                perfil="verificado";
                error="false";
        if perfil=="":
            time.sleep(1);
            intentos-=1;
            if intentos>=1:
                print("\nError, Ingrese usuario y contrasena nuevamente...\n");
            if intentos==0:
                volver="no";

    while perfil=="verificado":
        time.sleep(1);
        menu_principal();
        opcion1=int(input("indique operacion a realizar: "));
        while opcion1>5 and opcion1<1:
            time.sleep(1);
            print("\nIngrese una opcion valida\n");
            menu_principal();
            opcion1=int(input("indique operacion a realizar: "));
        time.sleep(1.5);
        if opcion1==1:
            print("\nHas ingresado para consultar tu Saldo Actual\n")
            time.sleep(1);
            print (f'Tu saldo actual es de {saldo_actual} pesos');
            time.sleep(1.5);
        elif opcion1==2:
            print("\nHas ingresado para realizar un deposito\n")
            time.sleep(1);
            menu_cantidades();
            opcion2=int(input("indique una cantidad: "));
            while opcion2>5 and opcion2<1:
                time.sleep(1);
                print("\nIngrese una opcion valida\n");
                menu_cantidades();
                opcion2=int(input("indique operacion a realizar: "));
            if opcion2==1:
                monto_deposito=50;
            elif opcion2==2:
                monto_deposito=100;
            elif opcion2==3:
                monto_deposito=200;
            elif opcion2==4:
                monto_deposito=500;
            if opcion2>=1 and opcion2<=4:
                time.sleep(1);
                print(f'\nUsted ha depositado {monto_deposito} pesos\n');
                saldo_actual=saldo_actual+monto_deposito;
                print(f'Tu saldo actual es de {saldo_actual} pesos');
        elif opcion1==3:
            print("\nHas ingresado para realizar un retiro\n")
            time.sleep(1);
            menu_cantidades();
            opcion2=int(input("indique una cantidad: "));
            while opcion2>5 and opcion2<1:
                time.sleep(1);
                print("\nIngrese una opcion valida\n");
                menu_cantidades();
                opcion2=int(input("indique operacion a realizar: "));
            if opcion2==1:
                if saldo_actual>=50:
                    monto_retiro=50;
                    transaccion="si";
                else:
                    transaccion="no";
            elif opcion2==2:
                if saldo_actual>=100:
                    monto_retiro=100;
                    transaccion="si";
                else:
                    transaccion="no";
            elif opcion2==3:
                if saldo_actual>=200:
                    monto_retiro=200;
                    transaccion="si";
                else:
                    transaccion="no";
            elif opcion2==4:
                if saldo_actual>=500:
                    monto_retiro=500;
                    transaccion="si";
                else:
                    transaccion="no";
            if opcion2>=1 and opcion2<=4:
                time.sleep(1);
                if transaccion=="si":       
                    print(f'\nUsted ha retirado {monto_retiro} pesos\n');
                    saldo_actual=saldo_actual-monto_retiro;
                    print(f'Tu saldo actual es de {saldo_actual} pesos');
                else:
                    print("Monto no valido...");
        elif opcion1==4:
            print("\nHas ingresado para cambiar tu PIN actual\n")
            time.sleep(1);
            pin="";
            intentos=3;
            while pin=="" and intentos>=1:
                pin_anterior=str(input("Ingrese su PIN anterior: "));                
                for i in range(0,len(usuarios_registrados)):
                    if contrasena==pin_anterior:
                        contrasena_registrados[i]=contrasena;
                        pin="valido";
                if pin=="":
                    time.sleep(1);
                    intentos-=1;
                    if intentos>=1:
                        print("\nError, Ingrese PIN anterior nuevamente...\n");
            if pin=="valido":
                time.sleep(1);
                pin_actualizado=str(input("\nIngrese su nuevo PIN: "));
                print(f'\nPIN confirmado, su nuevo PIN es {pin_actualizado}');
                pin_usuario=pin_actualizado;

                for i in range(0,len(usuarios_registrados)):
                    if contrasena==pin_anterior:
                        contrasena_registrados[i]=pin_actualizado;

                volver="si";
                perfil="";
                error="";
        elif opcion1==5:
            perfil="finalizado";
            volver="no";
            print("\nHasta la proxima");
if intentos==0:
    print("\nCuenta Bloqueada");
        
