"""16. - Jornal de un Operario
Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turnoque el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.
"""
codigo_turno=int(input("Ingrese codigo de turno: '1' para diurno, 2 para nocturno: "));
horas_trabajo=float(input("Ingrese Horas trabajadas: "));
PAGO_NOCTURNO=float(40.60);
PAGO_DIURNO=float(35.50); 
if codigo_turno==1:
    print(f'El operario trabajo {horas_trabajo} horas en el turno diurno y su pago es de {PAGO_DIURNO*horas_trabajo}');
else:
    print(f'El operario trabajo {horas_trabajo} horas en el turno nocturno y su pago es de {PAGO_NOCTURNO*horas_trabajo}');