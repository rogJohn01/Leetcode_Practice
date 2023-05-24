# Write your MySQL query statement below


select buyer_id from sales s join product p 
on s.product_id = p.product_id 
group by buyer_id 
having sum(p.product_name = 's8' ) > 0 and sum(p.product_name ='iphone' ) = 0 