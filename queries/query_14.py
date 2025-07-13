sql_query = """
SELECT u.fullname, COUNT(t.user_id) as task_count
FROM users u
LEFT JOIN tasks t on u.id = t.user_id
GROUP BY u.fullname
ORDER BY task_count DESC;
"""