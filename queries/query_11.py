sql_query = """
SELECT t.title, t.description, s.name as status_name
FROM tasks t
INNER JOIN status s ON t.status_id = s.id
INNER JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com'
"""