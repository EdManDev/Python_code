import sqlite3

conn = sqLite3.connct('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(123456, '2019-01-01','Python', 5)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
