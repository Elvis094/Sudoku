from src.models.move import Move

class SudokuService:
    def __init__(self, board):
        self.board = board  # Referencia al objeto Board (estado del tablero)
        self.history = []   # Historial de jugadas realizadas
        self.redo_stack = []  # Pila para jugadas deshechas (para rehacer)

    def make_move(self, row, col, num):
        # Valida si la celda es inicial (no modificable)
        if self.board.is_initial(row, col):
            return False, "No puedes modificar una celda inicial."
        # Valida rango del número
        if not (1 <= num <= 9):
            return False, "El número debe estar entre 1 y 9."
        # Valida reglas de Sudoku (fila, columna, región)
        if not self.is_valid_move(row, col, num):
            return False, "Movimiento inválido: número repetido en fila, columna o región."
        prev = self.board.get_cell(row, col)  # Guarda el valor anterior
        self.board.set_cell(row, col, num)    # Realiza el movimiento
        self.history.append(("Nueva", row, col, prev, num))  # Guarda en historial
        self.redo_stack.clear()  # Al hacer una jugada nueva, se limpia el redo
        return True, "Movimiento realizado."

    def is_valid_move(self, row, col, num):
        # Verifica que el número no esté en la fila
        for c in range(9):
            if self.board.current[row][c] == num:
                return False
        # Verifica que el número no esté en la columna
        for r in range(9):
            if self.board.current[r][col] == num:
                return False
        # Verifica que el número no esté en la región 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if self.board.current[r][c] == num:
                    return False
        return True

    def undo(self):
        # Deshace la última jugada realizada
        if not self.history:
            return False, "No hay jugadas para deshacer."
        action, row, col, prev, num = self.history.pop()
        self.redo_stack.append((action, row, col, prev, num))  # Guarda para rehacer
        self.board.set_cell(row, col, prev)  # Restaura el valor anterior
        return True, "Deshecho."

    def redo(self):
        # Rehace la última jugada deshecha
        if not self.redo_stack:
            return False, "No hay jugadas para rehacer."
        action, row, col, prev, num = self.redo_stack.pop()
        self.board.set_cell(row, col, num)  # Aplica el valor de nuevo
        self.history.append((action, row, col, prev, num))  # Vuelve a poner en historial
        return True, "Rehecho."

    def suggest(self, row, col):
        # Sugiere un número válido para la celda seleccionada
        if self.board.is_initial(row, col):
            return None
        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                return num  # Devuelve el primer número válido encontrado
        return None  # Si no hay sugerencia posible

    def get_history(self):
        # Devuelve el historial de jugadas en formato legible para el frontend
        return [
            {
                "tipo": action,
                "fila": row,
                "columna": col,
                "anterior": prev,
                "nuevo": num
            }
            for (action, row, col, prev, num) in self.history
        ]

# Si necesitas cambiar la lógica de validación, sugerencias, o historial,
# modifica los métodos correspondientes.
# Si quieres guardar más información en el historial, ajusta las tuplas y el formato del diccionario.
