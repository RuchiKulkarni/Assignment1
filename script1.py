import sqlite3
conn = sqlite3.connect('database.db')
conn.execute('''CREATE TABLE data
         (name           TEXT    NOT NULL,
         email           TEXT    NOT NULL,
         phoneno        INT NOT NULL,
         age            INT     NOT NULL,
         date         INT);''')
print("Table created successfully")
conn.close()
