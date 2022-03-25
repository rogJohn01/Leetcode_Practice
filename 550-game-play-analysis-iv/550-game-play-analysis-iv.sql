# Write your MySQL query statement below

select round(sum(event_date = min_date +1 )/count(distinct player_id) ,2)
	fraction 
from 
(select player_id , event_date, min(event_date) over (partition by player_id ) min_date from Activity ) t 