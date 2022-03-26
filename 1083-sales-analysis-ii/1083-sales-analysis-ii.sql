# Write your MySQL query statement below

select s.buyer_id from sales s left join product p
on s.product_id = p.product_id
group by s.buyer_id 
having sum(p.product_name = 'S8') >0 and sum(p.product_name ='iphone') =0 