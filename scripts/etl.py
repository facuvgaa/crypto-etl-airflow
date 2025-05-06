import requests
import os
import pandas as pd
import sqlite3
import time
import subprocess
import logging
from datetime import datetime

logging.basicConfig(filename="etl.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def log_message(message, level="info"):
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    print(message)

def extraccioData():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 5, "page": 1}
    response = requests.get(url, params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("error en los datos")
        return []

def dataTransform(cryptoData):
    df = pd.DataFrame(cryptoData)
    df = df[["id", "symbol", "name", "current_price", "market_cap", "total_volume"]]
    df["symbol"] = df["symbol"].str.upper()
    return df

def dataLoad(df):
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_DIR = os.path.join(BASE_DIR, 'db')
    DB_PATH = os.path.join(DB_DIR, 'crypto.db')
    
    

    print(f"ETL [DEBUG] BASE_DIR: {DB_PATH}") 
    if not os.path.exists(DB_PATH):
        print(f"[INFO] La base de datos no existe. Ejecutando createTable.py para crearla.")
        create_table_script = os.path.join(os.path.dirname(__file__), 'createTable.py')
        subprocess.run(['python', create_table_script], check=True)
    else:
        print(f"[INFO] La base de datos ya existe en: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    df["timestamp"] = time.time()
    df["timestamp"] = df["timestamp"].apply(lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))

    for _, row in df.iterrows():
        symbol = row["symbol"]
        price = row["current_price"]
        market_cap = row["market_cap"]
        volume = row["total_volume"]
        timestamp = row["timestamp"]

        cursor.execute("""
            SELECT current_price FROM cryptos WHERE symbol = ? AND timestamp LIKE ?
            ORDER BY timestamp DESC LIMIT 1
        """, (symbol, timestamp[:16] + "%"))

        result = cursor.fetchone()

        if result:
            last_price = result[0]
            if last_price != price:
                cursor.execute("""
                    UPDATE cryptos SET current_price = ?, market_cap = ?, total_volume = ?
                    WHERE symbol = ? AND timestamp LIKE ?
                """, (price, market_cap, volume, symbol, timestamp[:16] + "%"))
                print(f"🔄 Precio actualizado {symbol}: {last_price} ➡ {price}")
        else:
            cursor.execute("""
                INSERT INTO cryptos (name, symbol, current_price, market_cap, total_volume, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (row["name"], symbol, price, market_cap, volume, timestamp))
            print(f"✅ Nuevo registro guardado para {symbol}")

    conn.commit()
    conn.close()
    print("✅ Datos guardados correctamente en la base de datos")

def validate_data(df):
    if df.empty:
        print("⚠️ Advertencia: El DataFrame está vacío.")
        return False
    if df.isnull().values.any():
        print("⚠️ Advertencia: Hay valores nulos en los datos.")
        return False
    if (df["current_price"] <= 0).any():
        print("⚠️ Advertencia: Hay precios negativos o en cero.")
        return False
    print("✅ Datos validados correctamente")
    return True

def etl():
    log_message("⏳ Ejecutando ETL...")
    cryptoData = extraccioData()
    if not cryptoData:
        log_message("❌ Error: No se pudo extraer datos", "error")
        return
    crypto_df = dataTransform(cryptoData)
    if validate_data(crypto_df):
        dataLoad(crypto_df)
        log_message("✅ ETL completado correctamente")
    else:
        log_message("❌ ETL detenido por errores en los datos", "error")

if __name__ == "__main__":
    etl()
 
