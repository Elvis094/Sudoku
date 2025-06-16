class Board:
    """
    Clase que representa el tablero de Sudoku.
    Guarda el estado inicial y el estado actual del tablero.
    """

    def __init__(self, initial):
        # Copia profunda del tablero inicial para evitar modificaciones accidentales
        self.initial = [row[:] for row in initial]  # Estado original (no se puede modificar)
        self.current = [row[:] for row in initial]  # Estado actual (puede cambiar con las jugadas)

    def is_initial(self, row, col):
        # Devuelve True si la celda es parte del tablero inicial (no editable)
        return self.initial[row][col] != 0

    def set_cell(self, row, col, num):
        # Asigna un valor a una celda del tablero actual
        self.current[row][col] = num

    def get_cell(self, row, col):
        # Obtiene el valor de una celda del tablero actual
        return self.current[row][col]

    def is_full(self):
        # Devuelve True si el tablero está completamente lleno (sin ceros)
        return all(all(cell != 0 for cell in row) for row in self.current)

    def to_dict(self):
        # Convierte el tablero a un diccionario para enviarlo al frontend
        return {
            "initial": self.initial,
            "current": self.current
        }

# Si necesitas agregar más funcionalidades (por ejemplo, reiniciar el tablero),
# puedes añadir métodos adicionales aquí.
# Si cambias la estructura del tablero, actualiza los métodos correspondientes.
