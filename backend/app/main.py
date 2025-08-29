# backend/app/main.py
from fastapi import FastAPI
from db import get_connection

app = FastAPI()

@app.get("/metrics")
def get_metrics():
    conn = get_connection()
    cur = conn.cursor()

    # 工單數量
    cur.execute("SELECT COUNT(*) as total_orders FROM orders")
    total_orders = cur.fetchone()["total_orders"]

    # 已完成工單
    cur.execute("SELECT COUNT(*) as done_orders FROM orders WHERE status='done'")
    done_orders = cur.fetchone()["done_orders"]

    # 平均處理時間
    cur.execute("SELECT AVG(processing_time_min) as avg_time FROM orders WHERE processing_time_min IS NOT NULL")
    avg_time = cur.fetchone()["avg_time"]

    conn.close()

    return {
        "total_orders": total_orders,
        "done_orders": done_orders,
        "avg_processing_time_min": round(avg_time, 2) if avg_time else None,
        "hihi": "hihi"
    }
