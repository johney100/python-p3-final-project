# models/__init__.py
import sqlite3

CONN = sqlite3.connect('television.db')
CURSOR = CONN.cursor()
