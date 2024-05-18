import sqlite3

conn = sqlite3.connect('klu.db')
cursor = conn.cursor()

cursor.execute("""
select p.ProductName,sum(Quantity) as Most_Popular from products p 
inner join orderitems o on p.ProductId = o.ProductId
group by o.ProductId
order by Most_Popular desc
limit 1;
""")
popular_product = cursor.fetchone()
print(popular_product)

conn.close()
