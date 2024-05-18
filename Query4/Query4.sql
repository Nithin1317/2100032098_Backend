-- 4. List the products purchased in a specific order (e.g., OrderID = 1).
-- Query 4

select o.OrderItemId,o.OrderId,p.*,o.Quantity  from orderitems o
inner join products p on p.ProductId = o.ProductId
order by OrderId asc;