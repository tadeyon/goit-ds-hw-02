sql_query = """
SELECT u.fullname, t.title, t.description, s.name as status_name
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';
"""