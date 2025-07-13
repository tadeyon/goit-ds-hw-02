import sqlite3
import queries.query_1
import queries.query_10
import queries.query_11
import queries.query_12
import queries.query_13
import queries.query_14
import queries.query_2
import queries.query_3
import queries.query_4
import queries.query_5
import queries.query_6
import queries.query_7
import queries.query_8
import queries.query_9

def connect_to_db():
    return sqlite3.connect('tasks-management.sqlite')

def execute_query(conn, query: str):
    cursor = conn.cursor()
    cursor.execute(query)
    print('Query was executed.')
    return cursor.fetchall()

def main():
    conn = connect_to_db()
    queries_dict = {
        '1': queries.query_1.sql_query,
        '2': queries.query_2.sql_query,
        '3': queries.query_3.sql_query,
        '4': queries.query_4.sql_query,
        '5': queries.query_5.sql_query,
        '6': queries.query_6.sql_query,
        '7': queries.query_7.sql_query,
        '8': queries.query_8.sql_query,
        '9': queries.query_9.sql_query,
        '10': queries.query_10.sql_query,
        '11': queries.query_11.sql_query,
        '12': queries.query_12.sql_query,
        '13': queries.query_13.sql_query,
        '14': queries.query_14.sql_query
    }
    
    query_number = input('Enter query number: ')
    execute_query(conn, queries_dict[query_number])

if __name__ == '__main__':
    main()
