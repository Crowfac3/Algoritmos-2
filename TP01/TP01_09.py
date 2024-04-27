"""
-----------------------------------------------------------------------------------------------
Título: TP01-09 | CAJONES DE NARANJAS
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción: Resolver el siguiente problema utilizando funciones: Un productor frutihortícola desea contabilizar sus cajones de 
naranjas según el peso para poder cargar el camión de reparto. La empresa cuenta con N camiones, y cada uno puede 
transportar hasta media tonelada (500 kilogramos). 
En un cajón caben 100 naranjas con un peso entre 200 y 300 gramos cada una. Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como jugo. 
Se solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos cajones se pueden 
llenar, cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto. 

Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.

Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del 
camión no debe ser inferior al 80%; en caso contrario el camión no será despachado por su alto costo.


Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def calcularCosecha(cosechaNaranjas):
    contadorPeso = 0
    pesoDespachar = 0
    contadorCajones = 0
    naranjaParaJugo = 0
    naranjasParaDespachar = 0
    for i in range(cosechaNaranjas):
        peso = random.randint(150,350)
        if peso <= pesoMinimoNaranja or peso >= pesoMaximoNaranja:
            naranjaParaJugo += 1
        else:
            naranjasParaDespachar += 1
            contadorPeso += peso
        if naranjasParaDespachar == NaranjasPorCajon:
            pesoDespachar += contadorPeso
            contadorCajones += 1
            contadorPeso = 0
            naranjasParaDespachar = 0


    return naranjaParaJugo, naranjasParaDespachar, contadorCajones, pesoDespachar


def calcularCantidadDeCamiones(pesoDespachar):
    camionesLlenos = pesoDespachar // maximaCargaCamiones
    if (pesoDespachar % maximaCargaCamiones) > minimaCargaCamiones:
        camionesLlenos += 1
    return camionesLlenos


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
cantidadDeCamiones = random.randint(1,10)


#CARGA DE CAMIONES
maximaCargaCamiones = 500 * 1000
minimaCargaCamiones = int(maximaCargaCamiones * 0.8)

#VALORES DE NARANJA
NaranjasPorCajon = 100
pesoMinimoNaranja = 200
pesoMaximoNaranja = 300

#CONTADORES
naranjasCosechadas = 0


nuevaCosecha = int(input("Ingrese la cantidad de de Narajas cosechadas: "))
naranjasCosechadas += nuevaCosecha

naranjaParaJugo, naranjasParaDespachar, cantidadDeCajones, pesoParaDespachar = calcularCosecha(naranjasCosechadas)

naranjasCosechadas = naranjasParaDespachar

print()
print("La cantidad de Naranjas para jugo es:", naranjaParaJugo)
print()
print("La cantidad de Cajones para despachar es:", cantidadDeCajones)
print()
print("El sobrante de Naranjas es:", naranjasParaDespachar)
print()
cantidadDeCamiones = calcularCantidadDeCamiones(pesoParaDespachar)
if  cantidadDeCamiones != 0:
    print("La cantidad de camiones a despachar es: ",cantidadDeCamiones)

    


