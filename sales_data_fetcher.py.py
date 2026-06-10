import requests
import sqlite3

API_URL = (
    "http://api.petpooja.com/V1/orders/get_sales_data/"
    "?app_key=srd2neaq1xg7bzc6uyk5jmwv98o4tpfh"
    "&app_secret=fd08934c5224af4c975015e599d60a74bf857b4a"
    "&access_token=0442e1ee9899bc3806f1a40be490af4ec5c6602a"
    "&restID=51wok2zxnsad"
    "&from_date=2025-01-20%2000:00:00"
    "&to_date=2025-01-20%2023:59:59"
)

DB_NAME = "sales_data.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        receipt_number TEXT,
        sale_date TEXT,
        transaction_time TEXT,
        sale_amount REAL,
        tax_amount REAL,
        discount_amount REAL,
        round_off REAL,
        net_sale REAL,
        payment_mode TEXT,
        order_type TEXT,
        transaction_status TEXT
    )
    """)

    conn.commit()
    conn.close()

def fetch_sales_data():
    try:
        response = requests.get(API_URL, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

def insert_sales_data(records):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for record in records:
        cursor.execute("""
        INSERT INTO sales_data (
            receipt_number,
            sale_date,
            transaction_time,
            sale_amount,
            tax_amount,
            discount_amount,
            round_off,
            net_sale,
            payment_mode,
            order_type,
            transaction_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            record.get("receipt_number"),
            record.get("receipt_date"),
            record.get("transaction_time"),
            float(record.get("invoice_amount", 0)),
            float(record.get("tax_amount", 0)),
            float(record.get("discount_amount", 0)),
            float(record.get("round_off", 0)),
            float(record.get("net_sale", 0)),
            record.get("payment_mode"),
            record.get("order_type"),
            record.get("transaction_status")
        ))

    conn.commit()
    conn.close()

def main():
    create_database()

    data = fetch_sales_data()

    if not data:
        print("No data received from API.")
        return

    sales_records = data.get("data", [])

    if not sales_records:
        print("No sales records found.")
        return

    insert_sales_data(sales_records)
    print(f"{len(sales_records)} records inserted successfully.")

if __name__ == "__main__":
    main()
