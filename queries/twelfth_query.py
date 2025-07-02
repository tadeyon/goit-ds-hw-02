import sqlite3

def execute_query(db_path: str, sql_query: str):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        return cursor.fetchall()

sql_query = """
SELECT * from tasks
WHERE description = '';
"""