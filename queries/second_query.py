import sqlite3

def execute_query(db_path: str, sql_query: str):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()

sql_query = """
SELECT t.id, t.title, t.description, s.name as status_name
FROM tasks t
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'new';
"""