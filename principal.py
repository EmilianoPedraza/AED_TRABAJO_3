from funciones.requerimientos import opcion1_cargar_tratamientos, opcion2_mostrar_resultados



def valid_n_range(a,b, msj='Ingrese opción:'):
    """
    Solicita un número entero hasta que se encuentre dentro del rango indicado.
    """
    while True:
        n = int(input(msj))
        if a <= n <=b:
            return n


def opciones():
    print('Opción 1: Cargar Tratamientos')
    print('Opción 2: Mostrar Resultados')


def principal():
    op = -1
    tratamientos = []
    ## PREGUNTAMOS EN CLASES
    opciones()
    while op != 0:
        op = valid_n_range(0,2)
        if op == 1:
            tratamientos = opcion1_cargar_tratamientos('tratamientos.csv')
        if op == 2:
            if len(tratamientos) != 0:
              opcion2_mostrar_resultados(tratamientos)

if __name__ == '__main__':
    principal()
