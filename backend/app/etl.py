# backend/app/etl.py   
import pandas as pd
import sqlite3
from datetime import datetime

DB_PATH = "orders.db"

def run_etl(csv_path="sample_orders.csv"):
    # 1. 讀取 CSV
    df = pd.read_csv(csv_path)

    # 2. 清理：轉換時間格式
    df["start_time"] = pd.to_datetime(df["start_time"])
    df["end_time"] = pd.to_datetime(df["end_time"], errors="coerce")

    # 3. 加欄位：處理時間 (分鐘)
    df["processing_time_min"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 60

    # 4. 寫入 SQLite
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("orders", conn, if_exists="replace", index=False)
    conn.close()

    print(f"✅ ETL 完成，資料已存入 {DB_PATH}")

if __name__ == "__main__":
    run_etl()
