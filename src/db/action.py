import sqlite3


def ghdb_insert(dork):
    conn = sqlite3.connect("./data/data.db")
    cur = conn.cursor()

    sql_query = "INSERT INTO ghdb (dork) VALUES (?)"
    values = (str(dork))
    cur.execute(sql_query, values)

    conn.commit()
    conn.close()
