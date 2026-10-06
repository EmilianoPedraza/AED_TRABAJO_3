from funciones.requerimientos import opcion1_cargar_tratamientos, opcion2_mostrar_resultados
from funciones.validaciones import valid_option


def opciones():
    print('Opción 1: Cargar Tratamientos')
    print('Opción 2: Mostrar Resultados')


def principal():
    op = -1
    tratamientos = []
    while op != 0:
        ## PREGUNTAMOS EN CLASES
        opciones()
        op = valid_option(op, 0, 2)
        if op == 1:
            tratamientos = opcion1_cargar_tratamientos('tratamientos.csv')
        if op == 2:
            opcion2_mostrar_resultados(tratamientos)


if __name__ == '__main__':
    principal()
