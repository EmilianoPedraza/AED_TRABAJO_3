from funciones.procesamiento_tratamientos import procesar_tratamientos


def mostrar_result(r_n, val):
    """
    Muestra por pantalla un resultado identificado mediante una etiqueta.
    :param r_n: Identificador o número del resultado que se desea mostrar.
    :param val: Valor correspondiente al resultado.
    :return: None.
    """
    print(f'{r_n}: {val}')


def opcion1_cargar_tratamientos(f_d):
    """
    Carga los tratamientos desde el archivo 'tratamientos.csv' y muestra
    los resultados correspondientes a la cantidad de tratamientos cargados
    y al quinto tratamiento de alta complejidad.

    Si existe un quinto tratamiento de alta complejidad, muestra su apellido.
    En caso contrario, informa que no existen suficientes tratamientos de
    alta complejidad.
    :param f_d: File descrciptor
    :return: Lista de objetos Tratamiento obtenidos del archivo.
    """
    tratamientos, t_5_cmplj = procesar_tratamientos(f_d)
    mostrar_result('r1.1', len(tratamientos))
    if t_5_cmplj:  # si el quinto tratamiento es != 0 (false) entonces se encontro
        mostrar_result('r1.2', t_5_cmplj.apellido)
        return tratamientos
    mostrar_result('r1.2', 'No hay suficientes tratamientos de alta complejidad.')
    return tratamientos

if __name__ == '__main__':
    opcion1_cargar_tratamientos('../tratamientos.csv')
