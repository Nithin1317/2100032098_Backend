import sqlite3

conn = sqlite3.connect('klu.db')
cursor = conn.cursor()

cursor.execute("""
SELECT DATE_FORMAT(OrderDate, '%Y-%m') AS Month, 
       COUNT(Orders.OrderID) AS TotalOrders,
       SUM(Products.Price * OrderItems.Quantity) AS TotalSales
FROM Orders
JOIN OrderItems ON Orders.OrderId = OrderItems.OrderId
JOIN Products ON OrderItems.ProductId = Products.ProductId
WHERE YEAR(OrderDate) = 2023
GROUP BY DATE_FORMAT(OrderDate, '%Y-%m');
""")
monthly_sales = cursor.fetchall()
for month in monthly_sales:
    print(month)

conn.close()
