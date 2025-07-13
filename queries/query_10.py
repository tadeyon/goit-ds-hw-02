sql_query = """
SELECT s.name as status_name, COUNT(t.status_id) as task_count
FROM tasks t
INNER JOIN status s ON t.status_id = s.id
GROUP BY s.name
ORDER BY task_count DESC;
"""