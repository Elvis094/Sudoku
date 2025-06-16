def load_board_from_file(filename="board.txt"):
    """
    Lee un archivo de texto y carga un tablero de Sudoku como una matriz 9x9.
    - Cada línea representa una fila del tablero.
    - Los números representan celdas fijas.
    - El guion '-' representa una celda vacía (se convierte en 0).
    - Elimina espacios para soportar archivos con o sin espacios entre números.
    :param filename: Nombre del archivo a leer (por defecto 'board.txt').
    :return: Lista de listas (matriz) con los valores del tablero.
    """
    board = []
    with open(filename, "r") as f:
        for line in f:
            row = []
            for c in line.strip().replace(" ", ""):
                if c == "-":
                    row.append(0)  # Celda vacía
                else:
                    row.append(int(c))  # Celda con número fijo
            board.append(row)
    return board  # Devuelve la matriz del tablero

# Si necesitas cambiar el formato del archivo, ajusta la lógica dentro del bucle.
# Si el archivo está en otra ruta, cambia el valor por defecto de 'filename'.
