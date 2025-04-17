import sqlite3

conn = sqlite3.connect("crypto.db")
cursor = conn.cursor()

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

conn.commit()
conn.close()
print("✅ Tabla 'cryptos' creada correctamente.")