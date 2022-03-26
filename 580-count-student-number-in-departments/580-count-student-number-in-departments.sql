SELECT dept_name, SUM(CASE WHEN s.dept_id THEN 1 ELSE 0 END) as student_number
FROM department d LEFT JOIN student s ON d.dept_id = s.dept_id
GROUP BY 1
ORDER BY 2 desc, 1