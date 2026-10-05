def cond_may_min_q(n, a, b=None, min=False):
    """
    Evalúa si un número cumple una condición de comparación
    con un límite o con un rango.

    La función puede utilizarse de tres formas:

    - Si solo se proporciona `a` y `min` es False, verifica que `n`
      sea mayor o igual que `a`.
    - Si solo se proporciona `a` y `min` es True, verifica que `n`
      sea menor o igual que `a`.
    - Si se proporcionan `a` y `b`, verifica que `n` se encuentre
      dentro del rango [a, b], incluyendo ambos límites.

    :param n: Número que se desea evaluar.
    :param a: Límite inferior de la comparación o del rango.
    :param b: Límite superior del rango. Por defecto es None, indicando
              que no se está evaluando un rango.
    :param min: Define el tipo de comparación cuando no se utiliza un
                rango. Si es False, se evalúa n >= a; si es True,
                se evalúa n <= a.
    :return: True o False según si `n` cumple la condición.
             Devuelve -1 si se intenta utilizar `min=True` junto con
             un rango completo.
    """
    rang_complete = False
    if (a == 0 or a) and b != None:
        rang_complete = True

    if not rang_complete:  # Se valida un numero no un rango
        if not min:  # min False - se evalua que el numero sea mayor o igual que a
            return n >= a
        # min true - se evalua que el numero sea menor o igual que a
        return n <= a

    if min and b is not None:  # min no puede ser True si se esta por evaluar que un numero este dentro de un rango
        return -1

    return a <= n <= b


def valid_option(n, a, b=None, min=None, msj=['Ingrese opción:', 0], decimal=False):
    """
    Valida un número ingresado por el usuario según un límite o un rango.

    La función recibe un valor inicial y comprueba si cumple la condición
    establecida mediante `cond_may_min_q()`. Si el valor no es válido,
    solicita nuevamente al usuario un valor mediante `input()` y repite
    la validación hasta obtener uno que cumpla la condición.

    La validación puede realizarse de las siguientes formas:

    - Si `b` no se especifica y `min` es False, el valor debe ser mayor
      o igual que `a`.
    - Si `b` no se especifica y `min` es True, el valor debe ser menor
      o igual que `a`.
    - Si se especifican `a` y `b`, el valor debe encontrarse dentro del
      rango [a, b], incluyendo ambos límites.

    El tipo de dato solicitado al usuario depende de `decimal`:
    - Si `decimal` es False, se solicita un número entero mediante `int()`.
    - Si `decimal` es True, se solicita un número decimal mediante `float()`.

    :param n: Valor inicial que se desea validar.
    :param a: Límite inferior de la comparación o del rango.
    :param b: Límite superior del rango. Por defecto es None, indicando
              que no se utiliza un rango.
    :param min: Define el tipo de comparación cuando no se utiliza un
                rango. Si es False, se evalúa n >= a; si es True,
                se evalúa n <= a.
    :param msj: Lista que contiene los mensajes utilizados durante la
                solicitud de datos. El primer elemento se muestra al
                solicitar el valor y el segundo se muestra cuando el
                valor ingresado no cumple la condición.
    :param decimal: Indica si el valor solicitado debe ser decimal.
                    Si es False, se utiliza int(); si es True, float().
    :return: n
    """
    cond = True
    while cond:  # Inicialmente la condicion es true
        if not decimal:  # se solicita un entero
            n = int(input(msj[0]))
        else:  # se solicita un entero
            n = float(input(msj[0]))
        cond = not cond_may_min_q(n, a, b, min)
        if msj[1] and not cond:  # si la condicion no se cumple y existe un segundo mensaje
            print(msj[1])
    return n
