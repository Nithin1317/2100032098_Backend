-- Query 5
-- 5. Calculate the total amount spent by each customer.

select concat(c.FirstName,' ',c.LastName) as Customer_Name, sum(p.price*oi.Quantity) as Total_Amount_Spent 
from customers c
join orders o on o.CustomerId = c.CustomerId
join OrderItems oi on oi.OrderId = o.OrderId
join Products p on p.ProductId = oi.ProductId
group by Customer_Name;