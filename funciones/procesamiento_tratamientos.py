from clases.tratamiento import Tratamiento


def parsear_paciente(cadena):
    """
    Parsea una cadena de texto que contiene datos de un tratamiento
    y crea un objeto Tratamiento a partir de ellos.

    DNI, nombre, apellido, código, monto base, complejidad e ID.
    El monto base se convierte a float y el ID se convierte a int.

    :param cad: Cadena de texto que contiene los datos de un tratamiento
                separados por comas.
    :return: Objeto Tratamiento creado a partir de los datos de la cadena.
    """
    datos = cadena.split(',')
    dni, nom, apell, cod, mont_b, compl, id = datos  # Extraigo datos de la cadena

    
    return Tratamiento(dni, nom, apell, cod, float(mont_b), compl, int(id))


def procesar_tratamientos(r_file, prueba = False): #BORRAR ULTIMO PARAMETRO LUEGO
    """
    Lee y procesa un archivo de tratamientos, creando un objeto
    Tratamiento por cada registro leído.

    La primera línea del archivo se ignora, ya que corresponde al
    encabezado. Por cada línea restante se crea un objeto Tratamiento
    mediante la función `parsear_tratamiento()`.

    Además, cuenta los tratamientos de alta complejidad ('A') y obtiene
    el quinto tratamiento de alta complejidad encontrado.

    Si no existen cinco tratamientos de alta complejidad en el archivo,
    el segundo elemento de la tupla retornada será 0, caso contrario el elemento
    en cuestion será un Tratamiento.

    :param r_file: Ruta del archivo que contiene los datos de los
                   tratamientos.
    :return: Tupla formada por:
             - Primer elemento: Una lista con los objetos Tratamiento procesados;
             - Segundo elemento(valores posibles):
                    #Objeto: El quinto tratamiento de alta complejidad encontrado.
                    #Entero 0: Si no hay suficientes tratamientos de alta complejidad.

    """
    ts, file = [], open(r_file)
    # c es un contador que sirve para ignorar la primera linea del arhivo que se va a leer
    c = p_a_c_5 = cp_ac = 0
    for line in file:
        if c:
            t = parsear_paciente(line)  # Tratamiento
            #BORRAR LUEGO
            if prueba:
                print(t)
            if t.complejidad == 'A' and not p_a_c_5:  # cuento paciente de alta complejidad
                cp_ac += 1
            if cp_ac == 5 and not p_a_c_5:  # quinto paciente de alta complejidad
                p_a_c_5 = t
            ts.append(t)  # agrego al vector de registros de tratamientos
        if not c:
            c += 1
    file.close()
    return ts, p_a_c_5


if __name__ == '__main__':
    print(f'{'DNI':<15}' +
             f'{'NOMBRE':<15}' +
             f'{'APELLIDO':<12}' +
             f'{'COMPLEJIDAD':>4}' +
             f'{'CODIGO':>8}' +
             f'{'ID':^10}' +
             f'{'MONTO BASE':<2}')
    tratamientos = procesar_tratamientos('../tratamientos.csv', True) #BORRAR ULTIMO PARAMETRO LUEGO
    print('TRATAMIENTOS REGISTRADOS')
    print(tratamientos)