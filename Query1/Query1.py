import sqlite3

conn = sqlite3.connect('klu.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Customers")
customers = cursor.fetchall()
for customer in customers:
    print(customer)

conn.close()
