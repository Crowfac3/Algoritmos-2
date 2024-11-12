"""
-----------------------------------------------------------------------------------------------
Título: TP02-09 |  INTERCALACIÓN DE ELEMENTOS
Fecha: 04-2023
Autor: Adolfo German Garcia Bohl (1185420)

Descripción:
Intercalar los elementos de una lista entre los elementos de otra. La intercalación podrá realizarse utilizando el método
insert o mediante la técnica de rebanadas (slicing), y nunca se creará una lista nueva, sino que se modificará la primera.
Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden tener
distintas longitudes

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...
import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def juntarListas(_lista1, _lista2):
    
    for i in range(0, len(_lista2)):
        _lista1.insert((2*i+1),_lista2[i])
    
    return _lista1


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

lista1 = []
lista2 = []

longitudLista1 = random.randint(1,10)
longitudLista2 = random.randint(1,10)

for i in range (0, longitudLista1):
    lista1.append(random.randint(1,10))
for i in range (0, longitudLista2):
    lista2.append(random.randint(1,10)) 

print(lista1)
print(lista2)

listaNueva = juntarListas(lista1, lista2)

print(listaNueva)



