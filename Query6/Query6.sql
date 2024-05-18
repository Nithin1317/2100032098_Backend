-- Query 6
-- 6. Find the most popular product (the one that has been ordered the most).

select p.ProductName,sum(Quantity) as Most_Popular from products p 
inner join orderitems o on p.ProductId = o.ProductId
group by o.ProductId
order by Most_Popular desc
limit 1;