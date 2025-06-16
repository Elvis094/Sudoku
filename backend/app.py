# Importa Flask para crear la aplicación web
from flask import Flask
# Importa CORS para permitir peticiones desde el frontend (React)
from flask_cors import CORS
# Importa el blueprint que contiene las rutas del Sudoku
from src.controllers.sudoku_controller import bp

# Crea la instancia principal de la aplicación Flask
app = Flask(__name__)
# Habilita CORS para permitir comunicación entre frontend y backend
CORS(app)
# Registra el blueprint de Sudoku en la aplicación
app.register_blueprint(bp)

# Inicia la aplicación si este archivo es ejecutado directamente
if __name__ == "__main__":
    # Ejecuta el servidor en modo debug y acepta conexiones externas
    app.run(debug=True, host="0.0.0.0")