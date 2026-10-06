from funciones.procesamiento_tratamientos import procesar_tratamientos


def mostrar_result(r_n, val):
    """
    Muestra por pantalla un resultado identificado mediante una etiqueta.
    :param r_n: Identificador o número del resultado que se desea mostrar.
    :param val: Valor correspondiente al resultado.
    :return: None.
    """
    print(f'{r_n}: {val}')

def obtener_posicion_letra(letra):
  letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for i in range(len(letras)):
    if letra.upper() == letras[i].upper():
      return i
  return -1

def obtener_letra_con_posicion(indice):
  letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  if indice > len(letras) - 1 or indice < 0:
    return ""
  return letras[indice]

def opcion2_mostrar_resultados(tratamientos):
  total_dif = 0
  mas_tratamientos = [0] * 26
  mayor_monto_final = 0
  dni_tratamiento_final = 0
  
  for i in range(len(tratamientos)):
    tratamiento = tratamientos[i]

    total_dif += tratamiento.monto_final - tratamiento.monto_base
    mas_tratamientos[obtener_posicion_letra(tratamiento.codigo[0])] += 1

    if tratamiento.complejidad == "A" and mayor_monto_final < tratamiento.monto_final:
      mayor_monto_final = tratamiento.monto_final

      ## PREGUNTAR EN CLASES SOBRE QUE PASA SI NO HAY
      dni_tratamiento_final = tratamiento.dni

    

  max_value = 0
  letra_mayor = ""
  for i in range(len(mas_tratamientos)):
    if max_value < mas_tratamientos[i]:
      letra_mayor = obtener_letra_con_posicion(i)
      max_value = mas_tratamientos[i]



  mostrar_result("r.2.1", int(total_dif // len(tratamientos)))
  mostrar_result("r.2.2", letra_mayor)
  mostrar_result("r.2.3", max_value)
  mostrar_result("r.2.4", dni_tratamiento_final)
  

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
