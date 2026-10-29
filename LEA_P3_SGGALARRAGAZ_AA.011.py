# Fig. 7.2 Modificada: Inicialización dinámica de un arreglo.
import sys

def main():
    # Estructura selectiva para validar el argumento de línea de comandos
    # Si la longitud de sys.argv es mayor a 1, significa que el usuario pasó un tamaño
    if len(sys.argv) > 1:
        tamano_arreglo = int(sys.argv[1])
    else:
        tamano_arreglo = 10  # Valor predeterminado solicitado

    # Creación del arreglo estático con ceros según el tamaño determinado
    datos_arreglo = [0] * tamano_arreglo

    # Impresión de los encabezados de columnas con formato alineado
    print(f"{'Índice':>6} {'Valor':>8}")

    # Estructura repetitiva para recorrer e imprimir el contenido del arreglo
    for indice in range(len(datos_arreglo)):
        print(f"{indice:>6} {datos_arreglo[indice]:>8}")

# Control de ejecución de la función principal
if __name__ == "__main__":
    main()