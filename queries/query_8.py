sql_query = """
SELECT fullname, email
FROM users
WHERE email LIKE '%@example.org'
ORDER BY fullname;
"""