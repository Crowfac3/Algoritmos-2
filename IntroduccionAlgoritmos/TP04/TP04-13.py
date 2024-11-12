"""
-----------------------------------------------------------------------------------------------
Título: TP04-13 | BARAJA ESPAÑOLA
Fecha: 5-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Escribir un programa para crear mediante listas por comprensión los naipes de la baraja española de 48 cartas. La lista
debe contener cadenas de caracteres. Ejemplo: ["1 de Oros", "2 de Oros"... ]. Imprimir la lista por pantalla. (investigar en
internet el tema “python listas por comprensión producto cartesiano de dos listas”)


Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
palos = ["Oros", "Copas", "Espadas", "Bastos"]

barajaEspañola = [f"{numero} de {palo}" for numero in numeros for palo in palos]

for baraja in barajaEspañola:
    print(baraja)
