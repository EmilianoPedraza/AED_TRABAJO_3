class Tratamiento:
    """
    Representa un tratamiento médico realizado a un paciente.

    Cada objeto Tratamiento contiene los datos identificatorios del paciente,
    el código correspondiente al tratamiento y la información relacionada
    con su monto y nivel de complejidad.

    :param dni: Número de DNI del paciente, expresado como entero y sin puntos.
    :param nombre: Nombre del paciente.
    :param apellido: Apellido del paciente.
    :param codigo: Código ICD-10 correspondiente al tratamiento.
    :param monto_base: Monto base o mínimo a pagar por el tratamiento,
                       expresado como número decimal.
    :param complejidad: Carácter que indica el nivel de complejidad del
                        tratamiento. 'A' representa alta complejidad y
                        'R' representa complejidad regular.
    :param id: Identificador del tratamiento.
    """

    def __init__(self, dni, nombre, apellido, codigo, monto_base, complejidad, id):
        self.dni = dni  # numero entero pero sin puntos
        self.nombre = nombre  # cadena de caracteres
        self.apellido = apellido  # cadena de caracteres
        self.codigo = codigo  # codigo ICD10
        self.monto_base = monto_base  # Número flotante que representa el monto
        # base/mínimo a pagar por el tratamiento
        self.complejidad = complejidad  # Un caracter que representa si es de alta
        # complejidad o no. El caracter “A” representa un tratamiento de alta complejidad, el
        # caracter “R” representa un tratamiento regular.
        self.id = id

    def __str__(self):
        return (f'{self.dni:<15}' +
                f'{self.nombre:<15}' +
                f'{self.apellido:<15}' +
                f'{self.complejidad:^8}' +
                f'{self.codigo:<5}' +
                f'{self.id:^10}' +
                f'{self.monto_base:<10}')
