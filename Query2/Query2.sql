-- Query 2
-- 2. Find all orders placed in January 2023.

select * from orders
where month(OrderDate) = 1 and year(OrderDate) = 2023;