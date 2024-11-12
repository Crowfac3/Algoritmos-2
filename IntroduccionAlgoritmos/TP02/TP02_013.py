"""
-----------------------------------------------------------------------------------------------
Título: TP02-13 | REGISTRO DE VISITAS DE SOCIOS
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga.
Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola vez en el informe).
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los registros de entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------

def vecesIngreso(_listaIngresoSocios):
    """"Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola vez en el informe)."""
    listaSociosUnicos = []
    for socio in _listaIngresoSocios:
        if socio not in listaSociosUnicos:
            listaSociosUnicos.append(socio)
    
    for socio in listaSociosUnicos:
        vecesIngreso = _listaIngresoSocios.count(socio)
        print(f"Socio {socio} ingresó {vecesIngreso} veces al club.")


def eliminarSocio(_listaIngresoSocios, _socioBaja):
    """
    Elimina los registros de un socio de la lista de ingresos y devuelve la lista actualizada.
    """
    ingresosEliminados = 0
    listaActualizada = []
    for ingreso in _listaIngresoSocios:
        if ingreso != _socioBaja:
            listaActualizada.append(ingreso)
        else:
            ingresosEliminados += 1
    return listaActualizada, ingresosEliminados
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

listaingresoSocios = []
listaSociosNueva = []
numeroIngresosEliminados = 0

while True:
    numeroSocio = int(input("Ingrese número de Socio de 5 digitos (0 para finalizar): "))
    if numeroSocio == 0:
        break
    elif (numeroSocio < 10000) or (numeroSocio > 99999):
        print("El número de Socio debe tener 5 dígitos. Por favor, inténtalo de nuevo.")
        continue
    listaingresoSocios.append(numeroSocio)

vecesIngreso(listaingresoSocios)

while True:
    numeroSocioBaja = int(input("Ingrese número de Socio que se dio de Baja: "))
    if (numeroSocioBaja < 10000) or (numeroSocioBaja > 99999):
        print("El número de Socio debe tener 5 dígitos. Por favor, inténtalo de nuevo.")
        continue
    else:
        listaSociosNueva, numeroIngresosEliminados = eliminarSocio(listaingresoSocios, numeroSocioBaja)
        print(f"Se eliminaron {numeroIngresosEliminados} registros de ingreso para el socio {numeroSocioBaja}.")
        print("Los registros de ingreso al club antes de eliminar el socio son:")
        print(listaingresoSocios)
        print("Los registros de ingreso al club después de eliminar el socio son:")
        print(listaSociosNueva)
        break

