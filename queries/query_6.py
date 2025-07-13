sql_query = """
SELECT * FROM tasks
WHERE status_id != 3;
"""

sql_query_2 = """
    SELECT t.id, t.title, t.description, t.status_id, s.id as status_id, s.name as status_name
    FROM tasks t
    INNER JOIN status s ON t.status_id = s.id
    WHERE s.name != 'completed';
"""