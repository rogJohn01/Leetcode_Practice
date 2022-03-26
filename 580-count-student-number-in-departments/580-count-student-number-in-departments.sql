# Write your MySQL query statement below


select d.dept_name , ifnull( count(s.student_id) ,0) as student_number from student s right  join department d 
on d.dept_id = s.dept_id 
group by d.dept_name 
order by student_number desc  , d.dept_name 

