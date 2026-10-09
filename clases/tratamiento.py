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
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.codigo = codigo
        self.monto_base = monto_base
        self.complejidad = complejidad
        self.id_algoritmo = id

        codigo_porcentaje = int(codigo[4:])

        # algoritmos de cálculo del monto final-id 1
        if id == 1:
            porcentaje_extra = suma_fija = 0
            # si monto_base <= 60000 el porcentaje_extra queda en 0.
            # Si es mayor, el porcentaje se calcula en forma normal
            # N% de monto_base + adicional, no un 1% fijo.
            if (monto_base > 60000):
                # adicional fijo por letra del ICD10 (cálculo normal)
                if "A" <= codigo[0] <= "L":
                    monto_al = 25000
                elif codigo[0] == "U":
                    monto_al = 100000
                else:
                    monto_al = 40000
                porcentaje_extra = (monto_base + monto_al) * codigo_porcentaje / 100
                # la suma fija va para toda alta complejidad que no sea U
                # antes estaba dentro de un elif y solo valía para letras fuera de A-L.
                if self.complejidad == "A" and codigo[0] != "U":
                    suma_fija = monto_base / 2

            # El adicional ya no se suma al final (la tabla pide
            # monto_base + porcentaje_extra + suma_fija).
            self.monto_final = monto_base + porcentaje_extra + suma_fija
        # algoritmos de cálculo del monto final-id 2
        elif id == 2:
            porcentaje_extra = 0
            if "A" <= codigo[0] <= "P":
                # cálculo normal sin importar la complejidad
                # adicional fijo por letra del ICD10 (cálculo normal)
                if "A" <= codigo[0] <= "L":
                    monto_al = 25000
                elif codigo[0] == "U":
                    monto_al = 100000
                else:
                    monto_al = 40000
                porcentaje_extra = (monto_base + monto_al) * codigo_porcentaje / 100
            elif complejidad == "A":
                porcentaje_extra = monto_base * codigo_porcentaje * 2 / 100
            else:
                porcentaje_extra = monto_base * 15 / 100

            # monto_base + porcentaje_extra y no se modifica monto_base.
            self.monto_final = monto_base + porcentaje_extra
        # algoritmos de cálculo del monto final-id 3
        elif id == 3:
            monto_extra = 0
            monto_fijo = 0
            if complejidad == "A":
                monto_extra = monto_base * 30 / 100

            if "A" <= codigo[0] <= "L":
                monto_fijo = 20000
            elif "M" <= codigo[0] <= "P":
                monto_fijo = 15000 + 5000 * int(codigo[1:3])
            else:
                # CORREGIDO: era 100000 fijo, la tabla dice 10% del monto base
                monto_fijo = monto_base * 10 / 100

            # CORREGIDO: el tope de 60000 se aplica al monto_extra TOTAL
            # (30% + monto fijo), antes solo se limitaba el 30%.
            monto_extra = min(monto_extra + monto_fijo, 60000)
            self.monto_final = monto_base + monto_extra

        else:
            self.monto_final = monto_base
            if "A" <= codigo[0] <= "L":
                self.monto_final += 25000
            elif "M" <= codigo[0] <= "Z" and codigo[0] != "U":
                self.monto_final += 40000
            elif codigo[0] == "U":
                self.monto_final += 100000

            porcentaje = self.monto_final * codigo_porcentaje / 100

            self.monto_final += porcentaje

    def __str__(self):
        return (f'{self.dni:<15}' +
                f'{self.nombre:<15}' +
                f'{self.apellido:<15}' +
                f'{self.complejidad:^8}' +
                f'{self.codigo:<5}' +
                f'{self.id_algoritmo:^10}' +
                f'{self.monto_base:<10}' +
                f'{self.monto_final:<10}')
