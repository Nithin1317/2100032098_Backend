import sqlite3

conn = sqlite3.connect('klu.db')
cursor = conn.cursor()

cursor.execute("""
select c.*,o.OrderId,o.OrderDate from customers c 
inner join orders o on c.CustomerId = o.CustomerId;
""")
order_details = cursor.fetchall()
for detail in order_details:
    print(detail)

conn.close()
