import sqlite3

conn = sqlite3.connect("/home/amon/dev/cyberEngien/src/db/data/data.db")
cur = conn.cursor()

# Vérifier si la table "dork" existe déjà
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dork'")
table_exists = cur.fetchone()

if not table_exists:
    cur.execute("CREATE TABLE out (id INTEGER PRIMARY KEY, url TEXT UNIQUE, type TEXT)")
    cur.execute("CREATE TABLE dork (id INTEGER PRIMARY KEY, dork TEXT UNIQUE, type TEXT)")
    cur.execute("CREATE TABLE ghdb (id INTEGER PRIMARY KEY, dork TEXT UNIQUE)")
    conn.commit()

    
else:
    pass


conn.close()