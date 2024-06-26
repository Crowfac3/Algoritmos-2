"""
-----------------------------------------------------------------------------------------------
Título: TP04-14 | VERIFICACIÓN DE DIRECCIÓN DE EMAIL
Fecha: 5-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Se solicita crear un programa para leer direcciones de correo electrónico y verificar si representan una dirección válida.
Por ejemplo usuario@dominio.com.ar. Para que una dirección sea considerada válida el nombre de usuario debe poseer
solamente caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe tener al menos un carácter
y tiene que finalizar con “.com.ar”

Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mostrar un listado de todos los dominios, sin
repetirlos y ordenados alfabéticamente, recordando que las direcciones de mail no son case sensitive.


Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def validacionEmail(_mail):

    partes = _mail.split("@")
    if len(partes) != 2:
        return False

    usuario, dominio = partes

    print(partes)

    if not usuario.isalpha():
        return False

    if not dominio.endswith(".com.ar"):
        return False

    if len(dominio) < 7:
        return False
    
    return dominio


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

listaDominios = []

while True:
    print("Presione ENTER para terminar, sino")
    mail = input("Ingrese el email: ")
    if mail.strip() == "":
        break
    else:
        dominio = validacionEmail(mail)
        if dominio != False:
            listaDominios.append(dominio)
        continue

set(listaDominios)

for dominio in listaDominios:
    print(dominio)
