import sqlite3

conn = sqlite3.connect('klu.db')
cursor = conn.cursor()

cursor.execute("""
select o.OrderItemId,o.OrderId,p.*,o.Quantity  from orderitems o
inner join products p on p.ProductId = o.ProductId
order by OrderId asc;
""")
products = cursor.fetchall()
for product in products:
    print(product)

conn.close()
