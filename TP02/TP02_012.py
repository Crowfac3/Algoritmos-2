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
def registrarPaciente(numeroDeAfiliado, urgencia):
    if urgencia == 0:
        if numeroDeAfiliado in PacientesUrgentes:
            PacientesUrgentes[numeroDeAfiliado] += 1
        else:
            PacientesUrgentes[numeroDeAfiliado] = 1
    else:
        if numeroDeAfiliado in PacientesPorTurno:
            PacientesPorTurno[numeroDeAfiliado] += 1
        else:
            PacientesPorTurno[numeroDeAfiliado] = 1

def mostrarPacientesPorTipo():
    print("Pacientes atendidos por urgencia: ")
    for paciente, cantidad in PacientesUrgentes.items():
        print(f"{paciente}: {cantidad} veces")
    print("Pacientes atendidos por turno: ")
    for paciente, cantidad in PacientesPorTurno.items():
        print(f"{paciente}: {cantidad} veces")

def buscarPaciente(numeroDeAfiliado):
    if numeroDeAfiliado in PacientesUrgentes:
        contadorDeUrgencia = PacientesUrgentes[numeroDeAfiliado]
    else:
        contadorDeUrgencia = 0
    if numeroDeAfiliado in PacientesPorTurno:
        contadorDeTurno = PacientesPorTurno[numeroDeAfiliado]
    else:
        contadorDeTurno = 0
    print(f"Paciente {numeroDeAfiliado} atendido {contadorDeTurno} veces por turno y {contadorDeUrgencia} veces por urgencia")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
PacientesUrgentes = []
PacientesPorTurno = []



while True:
    numeroDeAfiliado = int(input("Ingrese número de afiliado (-1 para finalizar): "))
    if numeroDeAfiliado == -1:
        break
    urgencia = int(input("Ingrese 0 para urgencia o 1 para turno: "))
    registrarPaciente(numeroDeAfiliado, urgencia)
mostrarPacientesPorTipo()
while True:
    numeroDeAfiliado = int(input("Ingrese número de afiliado a buscar (-1 para finalizar): "))
    if numeroDeAfiliado == -1:
        break
    buscarPaciente(numeroDeAfiliado)