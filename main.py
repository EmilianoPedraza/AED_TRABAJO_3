from funciones.validaciones import valid_option
from funciones.requerimientos import opcion1_cargar_tratamientos


def opciones():
    print('Opción 1: Cargar Tratamientos')
    print('Opción 2: Mostrar Resultados:')


def principal():
    op = -1
    opciones()
    while op != 0:
        op = valid_option(op, 0, 2)
        if op == 1:
            opcion1_cargar_tratamientos('tratamientos.csv')
        if op == 2:
            pass


if __name__ == '__main__':
    principal()
