# backend/app/db.py
import sqlite3

DB_PATH = "orders.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # 讓結果可以 dict-like 存取
    return conn
