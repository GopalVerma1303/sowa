import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('textbook_qa.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS queries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  textbook TEXT,
                  query TEXT,
                  answer TEXT,
                  timestamp DATETIME)''')
    c.execute('''CREATE TABLE IF NOT EXISTS textbooks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  structure TEXT)''')
    conn.commit()
    conn.close()

def save_query(textbook, query, answer):
    conn = sqlite3.connect('textbook_qa.db')
    c = conn.cursor()
    c.execute("INSERT INTO queries (textbook, query, answer, timestamp) VALUES (?, ?, ?, ?)",
              (textbook, query, answer, datetime.now()))
    conn.commit()
    conn.close()

def get_query_history():
    conn = sqlite3.connect('textbook_qa.db')
    c = conn.cursor()
    c.execute("SELECT textbook, query, answer, timestamp FROM queries ORDER BY timestamp DESC")
    history = c.fetchall()
    conn.close()
    return history

def save_textbook_structure(name, structure):
    conn = sqlite3.connect('textbook_qa.db')
    c = conn.cursor()
    c.execute("INSERT INTO textbooks (name, structure) VALUES (?, ?)", (name, structure))
    conn.commit()
    conn.close()

def get_textbook_structure(name):
    conn = sqlite3.connect('textbook_qa.db')
    c = conn.cursor()
    c.execute("SELECT structure FROM textbooks WHERE name = ?", (name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None
