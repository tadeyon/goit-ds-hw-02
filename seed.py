import sqlite3
import faker

NUMBER_OF_USERS = 10
NUMBER_OF_TASKS = 100

def generate_fake_data(number_of_users, number_of_tasks):
    fake_users = []
    fake_tasks = []
    fake_data = faker.Faker()

    for _ in range(number_of_users):
        fake_users.append({
            "fullname": fake_data.name(),
            "email": fake_data.email(),
        })

    for _ in range(number_of_tasks):
        fake_tasks.append({
            "title": fake_data.text(max_nb_chars=50).strip(),
            "description": fake_data.text(),
            "status_id": fake_data.random_int(min=1, max=3),
            "user_id": fake_data.random_int(min=1, max=number_of_users),
        })
    
    return fake_users, fake_tasks

def seed_database(db_path: str, users: dict, tasks: dict):
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        sql_insert_user = "INSERT INTO users (fullname, email) VALUES (?, ?)"
        sql_insert_task = "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)"
        cursor.executemany(sql_insert_user, [(user['fullname'], user['email']) for user in users])
        cursor.executemany(sql_insert_task, [(task['title'], task['description'], task['status_id'], task['user_id']) for task in tasks])
        conn.commit()

if __name__ == "__main__":
    users, tasks = generate_fake_data(NUMBER_OF_USERS, NUMBER_OF_TASKS)
    seed_database('tasks-management.sqlite', users, tasks)