# EJEMPLOS DE TÉCNICAS DE CODIFICACIÓN

# =====================================================================================
# TÉCNICAS DE BUCLES DE VALIDACIÓN DE INPUT CON VERIFICACIÓN Y REINGRESO DEL DATO
# =====================================================================================

# Esta es una técnica de bucle de validación por "doble input"
valor = input("Ingrese el valor: ") # Si se trata del ingreso de números enteros usar "valor = int(input("Ingrese el valor: "))"
while valor != valorValido1 and valor != valorValido2 ...: # Si se trata de validar contra un rango numérico usar "if valor < valorMinimo or valor > valorMaximo:"
    valor = input("El valor ingresado es inválido, vuelva a intentar: ")


# Esta es una técnica de bucle de validación por "flag (bandera o centinela)"
flag = True
while flag:
    valor = input("Ingrese el valor: ") # Si se trata del ingreso de números enteros usar "valor = int(input("Ingrese el valor: "))"
    if valor == valorValido1 or valor == valorValido2 ...: # Si se trata de validar contra un rango numérico usar "if valor >= valorMinimo and valor <= valorMaximo:"
        flag = False
    else:
        print("El valor ingresado es inválido, vuelva a intentar.")


# Esta es una técnica de bucle de validación por "while True"
while True:
    valor = input("Ingrese el valor: ") # Si se trata del ingreso de números enteros usar "valor = int(input("Ingrese el valor: "))"
    if valor == valorValido1 or valor == valorValido2 ...: # Si se trata de validar contra un rango numérico usar "if valor >= valorMinimo and valor <= valorMaximo:"
        break
    else:
        print("El valor ingresado es inválido, vuelva a intentar.")


# =====================================================================================
# EJEMPLOS DE ELIMINACIÓN DE TODAS LAS APARICIONES DE DETERMINADO ELEMENTO EN UNA LISTA
# =====================================================================================

# Supongamos que se quieren eliminar todas las apariciones de "elementoEliminar" en "listaElementos"

# Esta técnica permite eliminarlos mediante el valor del elemento, usando el método remove
while elementoEliminar in listaElementos: 
    listaElementos.remove(elementoEliminar)


# Esta técnica es como la anterior, pero usa un "while" que itera siempre que la cantidad de "elementoEliminar" sea mayor a cero
while listaElementos.count(elementoEliminar) > 0:
    listaElementos.remove(elementoEliminar)


# Esta técnica permite eliminarlos mediante el índice del elemento, usando la sentencia "del" o el método "pop"
while elementoEliminar in listaElementos: 
    indice = listaElementos.index(elementoEliminar)
    del listaElementos[indice] # también se puede utilizar listaElementos.pop(indice)
# La técnica anterior es util cuando tenemos varias listas sincronizadas (que almacenan en las mismas posiciones datos relacionados)
# y queremos eliminar los elementos de una misma posición en todas las listas


# Esta técnica usa "lista por comprensión" creando una nueva lista que recibe solamente los elementos que no se deben eliminar
listaElementos = [elemento for elemento in listaElementos if elemento != elementoEliminar]
# también, para mutar la misma lista y no crear una nueva (es decir, no cambiarle la identidad), se puede utilizar:
# listaElementos[:] = [elemento for elemento in listaElementos if elemento != elementoEliminar]



# NUNCA USAR LA TÉCNICA DE BUCLE CON "RANGE" Y "LEN",
# YA QUE EN EL MOMENTO INICIAL CUANDO SE ENTRA AL FOR, PYTHON DETERMINA HASTA QUE VALOR LLEGARÁ EL INDICE, EN ESTE CASO SERÍA EL TAMAÑO DE LA LISTA,
# PERO LA LISTA SE IRÁ ACORTANDO A MEDIDA QUE SE VAYAN BORRANDO ELEMENTOS,
# CON LO CUAL EL INDICE TERMINARÁ MÁS ALLÁ DEL FINAL DE LA LISTA Y RESULTARÁ EN "IndexError: list assignment index out of range"

# NUNCA USAR ESTA ESTRUCTURA
for indice in range(len(listaElementos)):
    if listaElementos[indice] == elementoEliminar:
        del listaElementos[indice]

# BORRAR DESDE EL FINAL HACIA EL PRINCIPIO DE LA LISTA FUNCIONA, PERO LOS ARGUMENTOS SON MÁS DIFÍCILES DE INTERPRETAR
for indice in range(len(listaElementos)-1, -1, -1):
    if listaElementos[indice] == elementoEliminar:
        del listaElementos[indice]

# TAMPOCO NUNCA USAR LA TÉCNICA DE COMPROBACIÓN DE VALOR CON "IF",
# YA QUE, CUANDO SE ELIMINA UN ELEMENTO, EL SIGUIENTE ELEMENTO SE DESPLAZA A LA POSICIÓN DEL ELIMINADO,
# CON LO CUAL LA SIGUIENTE ITERACIÓN VA A SALTAR EL ELEMENTO DESPLAZADO Y NO LO VA A PROCESAR

# NUNCA USAR ESTA ESTRUCTURA
for elemento in listaElementos:
    if elemento == elementoEliminar:
        listaElementos.remove(elementoEliminar)

# NI TAMPOCO USAR ESTA ESTRUCTURA
for indice, elemento in enumerate(listaElementos):
    if elemento == elementoEliminar:
        del listaElementos[indice]


# =====================================================================================
# TÉCNICAS DE BUCLES DE VALIDACIÓN DE INPUT NUMÉRICO CON VERIFICACIÓN, REINGRESO DEL DATO (CON EXCEPCIONES)
# =====================================================================================

# Esta es una técnica de bucle de validación por "while True" para el ingreso de un número
# que no detiene el programa si se ingresa un texto, o si se da enter sin ingresar nada
while True:
    try:
        valor = int(input("Ingrese un número: ")) # Si se permiten decimales en el ingreso usar "valor = float(input("Ingrese un número: "))"
        if valor < valorMinimo or valor > valorMaximo: # Si se trata de validar contra valores discretos podemos usar "if valor not in listaValoresValidos:"
            raise ValueError
        break
    except ValueError:
        print("El valor ingresado es inválido, vuelva a intentar.")
        

# El mismo código anterior pero bajo la forma de una función
# con el mensaje de ingreso, el mensaje de error, y los valores válidos recibidos como parámetros
def ingresoNumero(_mensajeIngreso, _mensajeError, _valorMinimo, _valorMaximo): # Si se trata de validar contra valores discretos podemos usar "def ingresoNumero(_mensajeIngreso, _mensajeError, _listaValoresValidos):"
    while True:
        try:
            valor = int(input(_mensajeIngreso)) # Si se permiten decimales en el ingreso usar "valor = float(input(_mensajeIngreso))"
            if valor < _valorMinimo or valor > _valorMaximo: # Si se trata de validar contra valores discretos podemos usar "if valor not in _listaValoresValidos:"
                raise ValueError
            break
        except ValueError:
            print(_mensajeError)
    return valor

