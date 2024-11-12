"""
-----------------------------------------------------------------------------------------------
Título: TP02-12 | ATENCIÓN DE PACIENTES EN CLÍNICA
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se anuncia en la recepción
indicando su número de afiliado (número entero de 4 dígitos) y además indica si viene por una urgencia (ingresando un
0) o con turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en
el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por
urgencia. Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def registrarPaciente(pacientes_Urgentes, pacientes_Turno, numeroDeAfiliado, urgencia):
    if urgencia == 0:
        pacientes_Urgentes.append(numeroDeAfiliado)
    else:
        pacientes_Turno.append(numeroDeAfiliado)


def mostrarPacientesPorTipo(pacientes_Urgentes, pacientes_Turno):
    print("Pacientes atendidos por urgencia:")
    for paciente in pacientes_Urgentes:
        print(paciente)
    print("Pacientes atendidos por turno:")
    for paciente in pacientes_Turno:
        print(paciente)

def buscarPaciente(pacientes_Urgentes, pacientes_Turno, numeroDeAfiliado):
    veces_urgencia = pacientes_Urgentes.count(numeroDeAfiliado)
    veces_turno = pacientes_Turno.count(numeroDeAfiliado)
    print(f"El paciente {numeroDeAfiliado} fue atendido por urgencia {veces_urgencia} veces y por turno {veces_turno} veces.")
   
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
pacientesUrgentes = []
pacientesPorTurno = []



while True:
    numeroDeAfiliado = int(input("Ingrese número de afiliado (-1 para finalizar): "))
    if numeroDeAfiliado == -1:
        break
    elif (numeroDeAfiliado < 1000) or (numeroDeAfiliado > 9999):
        print("El número de afiliado debe tener 4 dígitos. Por favor, inténtalo de nuevo.")
        continue
    urgencia = int(input("Ingrese 0 para urgencia o 1 para turno: "))
    if urgencia not in [0, 1]:
        print("El valor de urgencia debe ser 0 o 1. Por favor, inténtalo de nuevo.")
        continue
    registrarPaciente(pacientesUrgentes, pacientesPorTurno, numeroDeAfiliado, urgencia)

mostrarPacientesPorTipo(pacientesUrgentes, pacientesPorTurno)

while True:
    numeroDeAfiliado = int(input("Ingrese número de afiliado a buscar (-1 para finalizar): "))
    if numeroDeAfiliado == -1:
        break
    buscarPaciente(pacientesUrgentes, pacientesPorTurno, numeroDeAfiliado)