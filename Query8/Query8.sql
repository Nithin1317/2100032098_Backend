-- Query 8
-- 8.Find customers who have spent more than $1000.

select concat(c.FirstName,' ',c.LastName) as Customer_Name,sum(p.price*oi.Quantity)  as Total_Amount_Spent 
from customers c
join orders o on o.CustomerId = c.CustomerId
join orderitems oi on oi.OrderId = o.OrderId
join products p on p.ProductId = oi.ProductId
group by Customer_Name
having  Total_Amount_Spent  > 1000;