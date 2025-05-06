import sqlite3
import pandas as pd
import os


def load_data(symbol = "BTC"):
       
       BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
       DB_DIR = os.path.join(BASE_DIR, 'db')

       DB_PATH = os.path.join(DB_DIR, "crypto.db")

    
       if not os.path.exists(DB_DIR):
              os.makedirs(DB_DIR)
       
       DB_PATH = os.path.join(DB_DIR, "crypto.db")
       conn = sqlite3.connect(DB_PATH)
       
       query = f"""
        SELECT timestamp, current_price FROM cryptos 
        WHERE symbol = '{symbol}'
        ORDER BY timestamp ASC
       """
       df = pd.read_sql(query, conn)
       conn.close()
       df["timestamp"] = pd.to_datetime(df["timestamp"])
       df["timestamp"] = df["timestamp"].astype("int64") // 10**9

       start_time = df["timestamp"].min()
       df["timestamp"] = (df["timestamp"] - df["timestamp"].min()) // 60


       
       return df, start_time