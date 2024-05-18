-- Query 7
-- 7. Get the total number of orders and the total sales amount for each month in 2023.

SELECT DATE_FORMAT(OrderDate, '%Y-%m') AS Month, 
       COUNT(Orders.OrderID) AS TotalOrders,
       SUM(Products.Price * OrderItems.Quantity) AS TotalSales
FROM Orders
JOIN OrderItems ON Orders.OrderId = OrderItems.OrderId
JOIN Products ON OrderItems.ProductId = Products.ProductId
WHERE YEAR(OrderDate) = 2023
GROUP BY DATE_FORMAT(OrderDate, '%Y-%m');