import sqlite3

def connect():
    return sqlite3.connect("database.db")

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY,
            customer TEXT,
            file TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_invoice(id, customer, file):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO invoices VALUES (?, ?, ?)", (id, customer, file))
    conn.commit()
    conn.close()

def get_last_invoice_id():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT MAX(id) FROM invoices")
    result = cur.fetchone()[0]
    conn.close()
    return result if result else 0

# Create table at import
create_table()
