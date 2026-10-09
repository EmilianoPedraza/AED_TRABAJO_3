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
        self.id_algoritmo = id


        codigo_porcentaje = int(codigo[4:])
        #algoritmos de cálculo del monto final-id 1
        if (id == 1):
          porcentaje_extra = suma_fija = monto_al = 0
          if (monto_base > 60000):
            if "A" <= codigo[0] <= "L":
              monto_al = 25000
            elif self.complejidad == "A" and codigo[0] != "U":
              ## Preguntar si es entero o no
              suma_fija = monto_base / 2

          porcentaje_extra = (monto_base + suma_fija + monto_al) / 100
          self.monto_final = monto_base + porcentaje_extra + suma_fija + monto_al
        #algoritmos de cálculo del monto final-id 2
        if (id == 2):
          porcentaje_extra = 0
          if "A" <= codigo[0] <= "P":
            porcentaje_extra = monto_base * codigo_porcentaje / 100

          if complejidad == "A":
            porcentaje_extra = monto_base * codigo_porcentaje * 2 / 100
          else:
            porcentaje_extra = monto_base * 15 / 100

          self.monto_final = monto_base = porcentaje_extra
        #algoritmos de cálculo del monto final-id 3
        if (id == 3):
          monto_extra = 0
          monto_fijo = 0
          if complejidad == "A":
            monto_extra = monto_base * 30 / 100

          if "A" <= codigo[0] <= "L":
              monto_fijo = 20000
          elif "M" <= codigo[0] <= "P":
              monto_fijo = 15000 + 5000 * int(codigo[1:3])
          else:
              monto_fijo+= 100000
          
          monto_extra = min(monto_extra, 60000)
          self.monto_final = monto_base + monto_extra + monto_fijo
          
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
