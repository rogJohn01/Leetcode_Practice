# Write your MySQL query statement below


select id from( select author_id as id from views 
              where author_id = viewer_id 
              order by id ) a
              group by id 
              order by id 