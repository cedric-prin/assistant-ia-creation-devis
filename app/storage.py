import sqlite3

DB_PATH = "data/devis.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS devis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT,
            client TEXT,
            email TEXT,
            date TEXT,
            contenu TEXT
        )
    """)
    conn.commit()
    conn.close()

def sauvegarder_devis(numero, client, email, date, contenu):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO devis (numero, client, email, date, contenu) VALUES (?, ?, ?, ?, ?)",
        (numero, client, email, date, contenu)
    )
    conn.commit()
    conn.close()
