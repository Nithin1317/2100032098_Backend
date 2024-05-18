import sqlite3

conn = sqlite3.connect('klu.db')
cursor = conn.cursor()

cursor.execute("""
select concat(c.FirstName,' ',c.LastName) as Customer_Name, sum(p.price*oi.Quantity) as Total_Amount_Spent 
from customers c
join orders o on o.CustomerId = c.CustomerId
join OrderItems oi on oi.OrderId = o.OrderId
join Products p on p.ProductId = oi.ProductId
group by Customer_Name;
""")
spending = cursor.fetchall()
for total in spending:
    print(total)

conn.close()
