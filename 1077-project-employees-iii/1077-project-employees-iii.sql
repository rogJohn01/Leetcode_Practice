

select p.project_id, p.employee_id
from Project p join Employee e
on p.employee_id = e.employee_id
where (p.project_id, e.experience_years) in (
    select a.project_id, max(b.experience_years)
    from Project a join Employee b
    on a.employee_id = b.employee_id
    group by a.project_id);

