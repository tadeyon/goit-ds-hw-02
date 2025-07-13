sql_query = """
SELECT t.id, t.title, t.description, s.name as status_name
FROM tasks t
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'new';
"""