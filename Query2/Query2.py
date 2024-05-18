import sqlite3

conn = sqlite3.connect('klu.db')
cursor = conn.cursor()

cursor.execute("""
select * from orders
where month(OrderDate) = 1 and year(OrderDate) = 2023
""")
orders = cursor.fetchall()
for order in orders:
    print(order)

conn.close()
