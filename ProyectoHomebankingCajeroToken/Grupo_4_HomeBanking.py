
                                        #HOME BANKING
#Variables:
#-------------usuariosDeHomeBanking
import time;
import random;
from datetime import timedelta
from datetime import date
from datetime import datetime
import datetime;

usuarios=[["tomasaguirre","1234567891234567891234"],["tomasperalta","3257839183647291874636"],["adrianafachal","8947367821341578392827"]];
empresas=["Edenor","Visa","Movistar","AYSA","Abl"];
monto_empresas=[1000,2000,1500,500,3500];
vencimiento=["01/06/2023","05/06/2023","09/06/2023","15/06/2023","21/06/2023"];
medios_de_pago=["Mercado Pago","Home Banking","Pago mis Cuentas"];
usuario_entrada=str();
verificacion_usuario=str();
intentos=int(3);
acceso_code=str();
saldo_inicial=int(100000);
saldo_actual=int(100000);
opcion_1=int();
titular_destino=str("Hombre X");
numero_control=int();
opcion_transaccion=int();
cbu_destino=int();
dato_erroneo="true";
moneda_pf=str("Pesos");
plazo_pf=int();
datos_completos_pf="si";
tna_pf=float(97);
tea_pf=float(154.28);
today=str();
sesion="";
dia_delta=int();\
contador=0;
#Fecha Plazo Fijo
meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
lista=[];
o="";
ano="";
mes="";
dia="";
mes_entero=int();
mes_actual=str();

#------------Importando TXT con claves 
with open("CodigoAcceso.txt") as archivo:
    for codigo in archivo:
        codigo_acceso=codigo;

with open("CodigoReautenticacion.txt") as archivo:
    for codigo in archivo:
        codigo_reaut=codigo;
with open("CodigoTransaccion.txt") as archivo:
    for codigo in archivo:
            codigo_transaccion=codigo;
#Funciones
def menu_home_banking():
    print("""

--------------------------------------------------------------------------------------------------------
        || 1) Transferencia  || 2)  Plazo       ||  3)    Pago de   ||  4)   Finalizar
        ||        Bancaria       ||       Fijo         ||        Servicios  ||         Sesion
--------------------------------------------------------------------------------------------------------
""");

#Algoritmo
print("""////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////BANCO UNIDO DEL GRUPO 4//////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
""");
while verificacion_usuario!="si" and intentos<=3 and intentos>=1:
    usuario_entrada=str(input("Ingresa tu Nombre de Usuario: "));
    usuario_entrada=usuario_entrada.lower().replace(" ","");
    for i in range(0,len(usuarios)):
        if usuario_entrada==usuarios[i][0]:
            verificacion_usuario="si";
            cbu_usuario=usuarios[i][1]
            intentos=2;
    if verificacion_usuario!="si":
        print("\nUsuario invalido...\n");
        intentos-=1;
if verificacion_usuario=="si":
    print("Usuario Valido\n");
    time.sleep(1);
    print("\t\tBANCO UNIDO DEL GRUPO 4\n");
    time.sleep(0.5);
    acceso_code=str(input("Ingresa el codigo de seguridad de Acceso: "));
    time.sleep(0.2);
    print("\nComprobando codigo ingresado, aguarde un momento...\n")
    time.sleep(1.5);
    while acceso_code!=codigo_acceso and intentos<=2 and intentos>=1:
        time.sleep(0.5);
        print("Codigo de Acceso de Seguridad Invalido, Intente nuevamente..\n")
        time.sleep(1.5)
        acceso_code=str(input("Ingresa el codigo de seguridad de Acceso: "));
        time.sleep(0.2);
        print("\nComprobando codigo ingresado, aguarde un momento...\n")
        time.sleep(1.5);
        if acceso_code!=codigo_acceso:
            intentos-=1;
    while acceso_code==codigo_acceso and sesion=="":
        time.sleep(1);
        print("""-----------------------------------------------------------------------------------------------------------------
                                Sea Bienvenido al BANCO UNIDO DEL GRUPO 4
        Bienvenido a la plataforma de Home Banking Numero 1 de Argentina
---------------------------------------------------------------------------------------------------------------------------""");
        menu_home_banking()
        opcion_1=int(input("Seleccione la opcion que desea realizar: "));
        while not(opcion_1>=1 and opcion_1<=3) and opcion_1!=4:
            time.sleep(1);
            print("Opcion Invalida, ingrese nuevamente");
            time.sleep(1);
            menu_home_banking()
            opcion_1=int(input("\nSeleccione la opcion que desea realizar: "));
        while dato_erroneo=="true":
            saldo_inicial=saldo_actual;
            if opcion_1==1:#TRANSFERENCIAS------------------------------------------------------------------
                print("\nNueva Transferencia\n");
                print(f'Desde: Caja de Ahorro {cbu_usuario}');
                print("\nEl CBU/CVU debe tener 22 digitos\n");
                cbu_destino=str(input("Ingrese Nuevo CBU/CVU a donde transferir: "));
                longitud_cbu=len(cbu_destino);
                time.sleep(1.5);
                while longitud_cbu!=22:
                    print("\nError\nEl CBU/CVU debe tener 22 digitos\n");
                    cbu_destino=str(input("Ingrese Nuevo CBU/CVU a donde transferir: "));
                    longitud_cbu=len(cbu_destino);
                    time.sleep(1.5);
                four_digitos=str();
                for i in range (longitud_cbu-3,longitud_cbu+1,1):
                    acumulador=(cbu_destino[i-1]);
                    four_digitos+=acumulador;
                cbu_txt=open("cbutxt.txt","w");
                string=repr(four_digitos);
                cbu_txt.write(string);
                cbu_txt.close();
                print();
                print("""Cuenta destino:
                1) Caja de Ahorro
                2) Cuenta Corriente
                """);
                opcion_cuenta_destino=int(input("Ingrese opcion valida: "));
                while opcion_cuenta_destino<1 and opcion_cuenta_destino>2:
                    print("\nOpcion no valida, intente nuevamente\n");
                    print("""Cuenta destino:
                    1) Caja de Ahorro
                    2) Cuenta Corriente
                    """);
                if opcion_cuenta_destino==1:
                    cuenta="Caja de Ahorro";
                elif opcion_cuenta_destino==2:
                    cuenta="Cuenta Corriente";
                print(f'\nUsted puede transferir hasta {saldo_actual} pesos');
                importe_transferencia=float(input("Ingrese Monto a Transferir: "));
                while importe_transferencia>saldo_inicial or importe_transferencia<1:
                    print("Monto Insuficiente o incorrecto, intente nuevamente...");
                    print(f'\nUsted puede transferir hasta {saldo_actual} pesos');
                    importe_transferencia=float(input("Ingrese Monto a Transferir: "));
                user_codigo_transaccion=str(input("\nIngresa los 6 digitos de su codigo se seguridad de transaccion: "))
                time.sleep(1);
                print("\nComprobando...");
                time.sleep(2);
                while codigo_transaccion!=user_codigo_transaccion:
                    print("\nCodigo de Transaccion Invalido, intente nuevamente")
                    time.sleep(1.3);
                    user_codigo_transaccion=str(input("Ingresa los 6 digitos de su codigo se seguridad de transaccion: "))
                if codigo_transaccion==user_codigo_transaccion:   
                    print("\nCodigo ingresado correctamente");
                    time.sleep(1);
                    print("\nVerificacion:\n");
                    print("------------------------------------------------------------------------------------------------");
                    print(f'Desde CBU: {cbu_usuario}');
                    print(f'Limite disponible: {saldo_actual}');
                    print(f'Titular de la cuenta destino: {titular_destino}');
                    print(f'Importe a transferir: {importe_transferencia} pesos');
                    print(f'Banco de la cuenta destino: Banco X');
                    print(f'Conceptos: Varios');
                    print("""
                    1) SI
                    2) NO, deseo modificar datos
                    """)
                    opcion_transaccion=int(input("Desea confirmar la transaccion?: "))
                    time.sleep(2);
                    while opcion_transaccion<=0 or opcion_transaccion>=3:
                        print("Ingrese opcion valida, intente nuevamente\n");
                        time.sleep(1);
                        print("""
                        1) SI
                        2) NO, deseo modificar datos
                        """)
                        opcion_transaccion=int(input("Desea confirmar la transaccion?: "))
                    if opcion_transaccion==2:
                        dato_erroneo="true";
                              
                    else:
                        dato_erroneo="false";
                        saldo_actual=saldo_inicial-importe_transferencia;
                        print("\nTransaccion Confirmada\n");
                        print(f'Su transferencia de ARS {importe_transferencia} desde su Caja de Ahorro {cbu_usuario}');
                        print(f'a {titular_destino} fue exitosa.');
                        print("Las transferencias a terceros tienen acreditacion inmediata las 24hs del dia , todos los dias del ano.")
                        print("------------------------------------------------------------------------------------------------------------");
                        numero_control=random.randrange(999,10000);
                        print(f'Numero de Control: {numero_control}');
                        print(f'Importe a transferir: {importe_transferencia} pesos');
                        print(f'CBU de la cuenta destino: {cbu_destino}');
                        print(f'Banco de la cuenta destino: Banco X');
                        print(f'Conceptos: Varios');
                        print("------------------------------------------------------------------------------------------------------------");
                        dato_erroneo="true";
                        menu_home_banking()
                        opcion_1=int(input("\nSeleccione la opcion que desea realizar: "));
            if opcion_1==2:#PLAZO FIJO--------------------------------------------------------------------------------------------------------
                saldo_inicial=saldo_actual;
                time.sleep(1);
                print("\n----------------------------------------------------------------------------")
                print("Constitucion del Plazo Fijo");
                print("----------------------------------------------------------------------------\n")
                print(f'Cuenta Debito - Caja de Ahorro - {cbu_usuario}');
                print("Operacion habilitada solo para Cajas de Ahorro.\nMonto minimo ARS 1000");
                print(f'Moneda del plazo fijo: {moneda_pf}');
                plazo_pf=int(input("Plazo en dias (Minimo 30 dias, Maximo 365 dias): "));
                time.sleep(1);
                while plazo_pf<30 or plazo_pf>365:
                    time.sleep(0.5);
                    print("\nDias invalidos, intente otra vez\n");
                    time.sleep(0.5);
                    plazo_pf=int(input("Plazo en dias (Minimo 30 dias, Maximo 365 dias): "));
                    time.sleep(1);
                print(f'\nUsted cuenta con {saldo_actual} pesos para realizar un Plazo FIjo');
                monto_pf=float(input("\nIngrese Monto (Minimo 1000 pesos): "));
                if monto_pf>saldo_actual or monto_pf <1000 or monto_pf<=0:
                    time.sleep(1);
                    print("\nIngrese Monto Valido");
                    print(f'Usted cuenta con {saldo_actual} pesos para realizar un Plazo FIjo');
                    monto_pf=float(input("Ingrese Monto (Minimo 1000 pesos): "));
                    datos_completos_pf="si";
                if datos_completos_pf=="si":
                    time.sleep(2);
                    print("\n----------------------------------------------------------------------------")
                    print("Verificacion");
                    print("----------------------------------------------------------------------------\n")
                    print("Producto:  Plazo Fijo");
                    print(f'Plazo:   {plazo_pf} dias');
                    print(f'Cuenta Debito:   Caja de Ahorro - {cbu_usuario}');
                    print(f'Tasa Nominal Anual: {tna_pf}%');
                    print(f'Tasa Efectiva Anual: {tea_pf}%');
                    intereses_pf=(monto_pf*tna_pf*plazo_pf)/36500;
                    print(f'Intereses a percibir:   {intereses_pf}');
                    print(f'Monto a depositar:   {monto_pf}');
                    today=str(date.today());
                    for i in range (0,len(today)):
                        o+=today[i];
                    r=str(o.split("-"));
                    lista.append(r);
                    for i in range (2,6):
                        ano+=(lista[0][i]);
                    for i in range (10,12):
                        mes+=(lista[0][i]);
                    for i in range (16,18):
                        dia+=(lista[0][i]);
                    mes_entero=(int(mes))-1;
                    mes_actual=meses[mes_entero];
                    print(f'Fecha de apertura:   {dia} {mes_actual} {ano}');
                    print("\nIngrese el codigo de Transaccion para confirmar: ");
                    user_codigo_transaccion=str(input("\nIngresa los 6 digitos de su codigo se seguridad de transaccion: "))
                    time.sleep(1);
                    print("\nComprobando...");
                    time.sleep(2);
                    while codigo_transaccion!=user_codigo_transaccion:
                        print("\nCodigo de Transaccion Invalido, intente nuevamente")
                        time.sleep(1.3);
                        user_codigo_transaccion=str(input("Ingresa los 6 digitos de su codigo se seguridad de transaccion: "))
                    if codigo_transaccion==user_codigo_transaccion:   
                        print("\nCodigo ingresado correctamente");
                        time.sleep(2);
                        print("\nSu Plazo Fijo se realizo correctamente\n");
                        print("Los depositos en pesos y en moneda extranjera cuentan con la garantia de hasta $1.500.000. ");
                        print("En las operaciones a nombre de dos o mas personas, la garantia se prorrateara entre su titulares.")
                        print("En ningun caso, el total de la garantia por persona y por deposito podra exceder de $1.500.000");
                        print("cualquiera sea el numero de cuentas y/o depositos.");
                        numero_control=random.randrange(999,10000);
                        print(f'\nNumero de referencia: {numero_control}');
                        print(f'Producto: Plazo Fijo');
                        print(f'Tasa de interes anual nominal: {tna_pf}%');
                        print(f'Tasa Efectiva Anual: {tea_pf}%');
                        print(f'Monto Capital:   {monto_pf}');
                        monto_total=monto_pf+intereses_pf;
                        print(f'Monto total (Capital + intereses):   {monto_total}');
                        print(f'Fecha de Alta:   {dia} {mes_actual} {ano}');
                        lista=[];
                        o="";
                        ano="";
                        mes="";
                        dia="";
                        mes_entero=int();
                        mes_actual=str();
                        dia_delta=datetime.timedelta(days=plazo_pf);
                        fecha_inicial=datetime.date.today();
                        fecha_futura=str(fecha_inicial+dia_delta);
                        for i in range (0,len(fecha_futura)):
                            o+=fecha_futura[i];
                        r=str(o.split("-"));
                        lista.append(r);
                        for i in range (2,6):
                            ano+=(lista[0][i]);
                        for i in range (10,12):
                            mes+=(lista[0][i]);
                        for i in range (16,18):
                            dia+=(lista[0][i]);
                        mes_entero=(int(mes))-1;
                        mes_actual=meses[mes_entero];
                        print(f'Fecha de vencimiento:   {dia} {mes_actual} {ano}\n');
                        lista=[];
                        o="";
                        ano="";
                        mes="";
                        dia="";
                        mes_entero=int();
                        mes_actual=str();
                        time.sleep(1);
                        saldo_actual=saldo_inicial-monto_pf;
                        print("""
                        ------------------------------------------------------------------------------------------------------------------------
                                                Sea Bienvenido al BANCO UNIDO DEL GRUPO 4
                                Bienvenido a la plataforma de Home Banking Numero 1 de Argentina
                        ---------------------------------------------------------------------------------------------------------------------------""");
                        menu_home_banking()
                        opcion_1=int(input("Seleccione la opcion que desea realizar: "));
                        
            if opcion_1==3:#Pago de Servicios--------------------------------------------------------------------------------------------------------
                saldo_inicial=saldo_actual;
                print("\nPago de Servicios\n");
                print("Para realizar pagos debera ingresar el codigo de reautenticacion generado\npor su dispositivo de Seguridad");
                codigo_reaut_entrada=str(input(f'\nIngrese Codigo de Reautenticacion: '));
                time.sleep(1.5);
                while codigo_reaut!=codigo_reaut_entrada:
                    print("\nError!, intente nuevamente...\n");
                    print("Para realizar pagos debera ingresar el codigo de reautenticacion generado\npor su dispositivo de Seguridad");
                    codigo_reaut_entrada=str(input(f'\nIngrese Codigo de Reautenticacion: '));
                    time.sleep(1.5);
                pago_servicios="si";
                while pago_servicios=="si":
                    print("\nProximos Vencimientos\n");
                    print("Selecciona el servicio que deseas pagar...\n");
                    for a in range(0,len(empresas)):
                        contador+=1;
                        print(f'{contador}) {empresas[a]}');
                    time.sleep(1);
                    opcion_ps=int(input("\nIngrese opcion a pagar: "));
                    while opcion_ps>len(empresas) or opcion_ps<1:
                        contador=0;
                        time.sleep(1);
                        print("Error..., Selecciona el servicio que deseas pagar...\n");
                        for a in range(0,len(empresas)):
                            contador+=1;
                            print(f'{contador}) {empresas[a]}');
                        opcion_ps=int(input("\nIngrese opcion a pagar: "));
                    servicio_pagar=empresas[opcion_ps -1];
                    precio_pagar=monto_empresas[opcion_ps -1];
                    vencimiento_servicio=vencimiento[opcion_ps -1];
                    time.sleep(1);
                    print(f'\nUsted ha seleccionado para pagar {servicio_pagar}');
                    time.sleep(1);
                    print(f'\nDebera abonar {precio_pagar} pesos');
                    print(f'Usted tiene disponible {saldo_actual} pesos en la cuenta\n');
                    print(f'{servicio_pagar} vence el dia {vencimiento_servicio}\n');
                    contador=0;
                    for a in range(0,len(medios_de_pago)):
                        contador+=1;
                        print(f'{contador}) {medios_de_pago[a]}');
                    opcion_pago=int(input("\nIngrese opcion a pagar: "));
                    time.sleep(1);
                    print(f'\nHas seleccionado {medios_de_pago[opcion_pago-1]} como forma de pago\n');
                    pago_servicios="";
                    time.sleep(2);
                    print("---------------------------------------------------------------------------------------");
                    print("\nEstas Pagando\n");
                    print(f'Servicio a Pagar: {servicio_pagar}');
                    print(f'Importe a Pagar: {precio_pagar}');
                    print(f'Vencimiento: {vencimiento_servicio}');
                    print(f'Medio de Pago: {medios_de_pago[opcion_pago-1]}\n');
                    print("---------------------------------------------------------------------------------------");
                    time.sleep(1.5);
                    continuar=int(input("\n1) Confirmar y continuar\n2) Modificar datos\nElija su opcion: "));
                    if continuar==1:
                        saldo_actual=saldo_inicial-precio_pagar;
                        time.sleep(1);
                        print("\n---------------------------------------------------------------------------------------");
                        print("\nPagos Efectuados\n");
                        print(f'Servicio: {servicio_pagar}');
                        print(f'Importe Pagado: {precio_pagar}');
                        print(f'Vencimiento: {vencimiento_servicio}');
                        print(f'Medio de Pago: {medios_de_pago[opcion_pago-1]}\n');
                        print("---------------------------------------------------------------------------------------\n");
                        time.sleep(2);
                        print("1) SI\n2) NO");
                        comprobante=int(input("\nDesea imprimir el comprobante?: "));
                        while comprobante!=1 and comprobante!=2:
                            time.sleep(1);
                            print("\nError, seleccione opcion valida\n");
                            print("1) SI\n2) NO");
                            comprobante=int(input("\nDesea imprimir el comprobante?: "));
                        if comprobante==1: 
                            pagos_txt=open("comprobante.txt","w");
                            pagos_txt.write("Pagos Efectuados:\n");
                            pagos_txt.write(f'Servicio: {servicio_pagar}\n');
                            pagos_txt.write(f'Importe Pagado: {precio_pagar}\n');
                            pagos_txt.write(f'Vencimiento: {vencimiento_servicio}\n');
                            pagos_txt.write(f'Medio de Pago: {medios_de_pago[opcion_pago-1]}\n');
                            pagos_txt.close();
                            time.sleep(1);
                            print("\nComprobante enviado, muchas gracias")
                            time.sleep(2);
                            contador=0;
                        else:
                            print("\nSesion finalizada\n");
                            time.sleep(2);
                    else:
                        print("\nModificar datos");
                        contador=0;
                        modificar="si";
                        
                if modificar!="si":
                    print("""
                    -----------------------------------------------------------------------------------------------------------------
                                        Sea Bienvenido al BANCO UNIDO DEL GRUPO 4
                            Bienvenido a la plataforma de Home Banking Numero 1 de Argentina
                    ---------------------------------------------------------------------------------------------------------------------------""");
                    menu_home_banking()
                    opcion_1=int(input("Seleccione la opcion que desea realizar: "));
                else:
                    modificar="";
            if opcion_1==4:
                sesion=="terminada";
                dato_erroneo="false";
                print("Usted ha salido de la Sesion, hasta pronto");
                sesion="terminada";
if intentos<1:
    print("Lamentamos Informar Que Su Cuenta Fue Bloqueada");

