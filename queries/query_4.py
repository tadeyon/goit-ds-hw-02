sql_query = """
SELECT * FROM users 
WHERE id NOT IN (
    SELECT t.user_id
    FROM tasks t
);
"""