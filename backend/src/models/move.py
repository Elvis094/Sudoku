class Move:
    """
    Clase que representa una jugada (movimiento) en el Sudoku.
    Guarda la fila, columna, número colocado y el tipo de acción (ej: 'Nueva', 'Deshacer', 'Rehacer').
    """

    def __init__(self, row, col, num, action):
        self.row = row      # Fila de la jugada (0-8)
        self.col = col      # Columna de la jugada (0-8)
        self.num = num      # Número colocado en la celda
        self.action = action  # Tipo de acción: 'Nueva', 'Deshacer', 'Rehacer', etc.

    def to_dict(self):
        """
        Convierte el movimiento a un diccionario para facilitar su envío al frontend o guardado.
        """
        return {
            "row": self.row,
            "col": self.col,
            "num": self.num,
            "action": self.action
        }

# Si necesitas guardar más información sobre la jugada (por ejemplo, valor anterior),
# agrega más atributos al constructor y al método to_dict.
