import sqlite3

def create_tables():
    with open('create_tables.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('tasks-management.sqlite') as conn:
        cursor = conn.cursor()
        cursor.executescript(sql)

if __name__ == "__main__":
    create_tables()