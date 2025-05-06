import sqlite3
import os

# Obtener la ruta de la carpeta 'scripts'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Crear la carpeta 'db' si no existe
DB_DIR = os.path.join(BASE_DIR, 'db')
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

# Ruta de la base de datos dentro de 'scripts/db'
DB_PATH = os.path.join(DB_DIR, 'crypto.db')

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Crear la tabla 'cryptos' si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS cryptos (
    id TEXT,
    symbol TEXT,
    name TEXT,
    current_price REAL,
    market_cap REAL,
    total_volume REAL,
    timestamp TEXT
)
""")

# Confirmar cambios y cerrar la conexión
conn.commit()
conn.close()

# Mostrar la ruta de la base de datos
print(f"[DEBUG] DB_PATH absoluto: {DB_PATH}")
print("✅ Tabla 'cryptos' creada correctamente.")
