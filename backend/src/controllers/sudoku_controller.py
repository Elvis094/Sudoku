from flask import Blueprint, request, jsonify
from src.models.board import Board
from src.services.sudoku_service import SudokuService
from src.utils.file_loader import load_board_from_file

# Crea un blueprint para agrupar las rutas relacionadas con Sudoku
bp = Blueprint('sudoku', __name__)

# Carga el tablero inicial desde el archivo board.txt
initial_board = load_board_from_file("board.txt")
board = Board(initial_board)  # Crea el objeto Board con el estado inicial
service = SudokuService(board)  # Crea el servicio que maneja la lógica del juego

@bp.route("/get_board", methods=["GET"])
def get_board():
    # Devuelve el tablero inicial y el actual al frontend
    return jsonify(board.to_dict())

@bp.route("/move", methods=["POST"])
def move():
    # Recibe una jugada del usuario y la procesa
    data = request.json
    row, col, num = data["row"], data["col"], data["num"]
    valid, msg = service.make_move(row, col, num)
    if not valid:
        # Si la jugada no es válida, devuelve un error y el mensaje correspondiente
        return jsonify({"success": False, "error": msg})
    finished = board.is_full()  # Verifica si el tablero está completo
    # Devuelve el tablero actualizado y si el juego terminó
    return jsonify({"success": True, "board": board.current, "finished": finished})

@bp.route("/undo", methods=["POST"])
def undo():
    # Deshace la última jugada realizada
    valid, msg = service.undo()
    if not valid:
        return jsonify({"success": False, "error": msg})
    return jsonify({"success": True, "board": board.current})

@bp.route("/redo", methods=["POST"])
def redo():
    # Rehace la última jugada deshecha
    valid, msg = service.redo()
    if not valid:
        return jsonify({"success": False, "error": msg})
    return jsonify({"success": True, "board": board.current})

@bp.route("/suggest", methods=["POST"])
def suggest():
    # Sugiere un número válido para la celda seleccionada
    data = request.json
    row, col = data["row"], data["col"]
    suggestion = service.suggest(row, col)
    if suggestion is None:
        return jsonify({"success": False, "error": "No hay sugerencia disponible"})
    return jsonify({"success": True, "suggestion": suggestion})

@bp.route("/history", methods=["GET"])
def get_history():
    # Devuelve el historial de jugadas realizadas
    return jsonify(service.get_history())

# Si necesitas agregar más funcionalidades (por ejemplo, reiniciar el tablero o cargar un nuevo tablero),
# puedes agregar nuevas rutas aquí y usar los métodos del servicio o del modelo Board.