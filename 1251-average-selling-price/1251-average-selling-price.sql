# Write your MySQL query statement below


select p.product_id , round(sum(u.units*p.price)/sum(u.units) ,2 ) as average_price from prices p join unitssold u
on p.product_id = u.product_id and p.start_date <= u.purchase_date and u.purchase_date <= p.end_date 
group by p.product_id 


