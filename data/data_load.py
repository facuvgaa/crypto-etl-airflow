import sqlite3
import pandas as pd


def load_data(symbol = "BTC"):
       conn = sqlite3.connect("crypto.db")
       
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

       print(f"aqui {df['timestamp'].head()}")

       
       return df, start_time