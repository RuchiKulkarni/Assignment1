import sqlite3
conn=sqlite3.connect('database.db')
cursor=conn.execute("SELECT name, email,phoneno, age, date from data")
while True:
   name=input("Enter a Name to Show data:\n")
   break
a=f"SELECT * FROM data WHERE name='{name}'"
data=cursor.execute(a)
for row in cursor:
   print(row[0],row[1],row[2],row[3],row[4])
if not a:
   print(f"User Data not found{name}")
conn.close()