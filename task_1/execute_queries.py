import psycopg2

def execute_queries():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="mysecretpassword",
        host="localhost"
    )
    cur = conn.cursor()

    # Отримати всі завдання певного користувача
    user_id = 1  # Змініть на потрібне значення ID користувача
    cur.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
    user_tasks = cur.fetchall()
    print("Tasks for user with ID {}: ".format(user_id))
    for task in user_tasks:
        print(task)

    # Вибрати завдання за певним статусом
    cur.execute("SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new')")
    new_tasks = cur.fetchall()
    print("New tasks:")
    for task in new_tasks:
        print(task)

    # Оновити статус конкретного завдання
    task_id = 1  # Змініть на потрібне значення ID завдання
    cur.execute("UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = %s", (task_id,))
    conn.commit()

    # Отримати список користувачів, які не мають жодного завдання
    cur.execute("SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks)")
    users_without_tasks = cur.fetchall()
    print("Users without tasks:")
    for user in users_without_tasks:
        print(user)

    # Додати нове завдання для конкретного користувача
    new_task_data = ("New Task", "Description of new task", 1, 1)  # Змініть на потрібні дані для нового завдання
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", new_task_data)
    conn.commit()

    # Отримати всі завдання, які ще не завершено
    cur.execute("SELECT * FROM tasks WHERE status_id <> (SELECT id FROM status WHERE name = 'completed')")
    incomplete_tasks = cur.fetchall()
    print("Incomplete tasks:")
    for task in incomplete_tasks:
        print(task)

    # Видалити конкретне завдання
    task_id_to_delete = 1  # Змініть на потрібне значення ID завдання для видалення
    cur.execute("DELETE FROM tasks WHERE id = %s", (task_id_to_delete,))
    conn.commit()

    # Знайти користувачів з певною електронною поштою
    email_domain = '%@example.com'  # Змініть на потрібний домен електронної пошти
    cur.execute("SELECT * FROM users WHERE email LIKE %s", (email_domain,))
    users_with_email_domain = cur.fetchall()
    print("Users with email domain '{}':".format(email_domain))
    for user in users_with_email_domain:
        print(user)

    # Оновити ім'я користувача
    user_id_to_update = 1  # Змініть на потрібне значення ID користувача для оновлення
    new_fullname = "New Fullname"  # Змініть на нове повне ім'я користувача
    cur.execute("UPDATE users SET fullname = %s WHERE id = %s", (new_fullname, user_id_to_update))
    conn.commit()

    # Отримати кількість завдань для кожного статусу
    cur.execute("""
        SELECT status.name, COUNT(tasks.id) AS task_count 
        FROM status 
        LEFT JOIN tasks ON status.id = tasks.status_id 
        GROUP BY status.name
    """)
    task_counts_by_status = cur.fetchall()
    print("Task counts by status:")
    for status, count in task_counts_by_status:
        print("{}: {}".format(status, count))

    # Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
    email_domain = '%@example.com'  # Змініть на потрібний домен електронної пошти
    cur.execute("""
        SELECT tasks.*
        FROM tasks
        JOIN users ON tasks.user_id = users.id
        WHERE users.email LIKE %s
    """, (email_domain,))
    tasks_for_users_with_email_domain = cur.fetchall()
    print("Tasks for users with email domain '{}':".format(email_domain))
    for task in tasks_for_users_with_email_domain:
        print(task)

    # Отримати список завдань, що не мають опису
    cur.execute("SELECT * FROM tasks WHERE description IS NULL OR description = ''")
    tasks_without_description = cur.fetchall()
    print("Tasks without description:")
    for task in tasks_without_description:
        print(task)

    # Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
    cur.execute("""
        SELECT users.fullname, tasks.title 
        FROM users 
        INNER JOIN tasks ON users.id = tasks.user_id 
        INNER JOIN status ON tasks.status_id = status.id 
        WHERE status.name = 'in progress'
    """)
    users_and_tasks_in_progress = cur.fetchall()
    print("Users and their tasks in progress:")
    for user, task in users_and_tasks_in_progress:
        print("{}: {}".format(user, task))

    # Отримати користувачів та кількість їхніх завдань
    cur.execute("""
        SELECT users.fullname, COUNT(tasks.id) AS task_count 
        FROM users 
        LEFT JOIN tasks ON users.id = tasks.user_id 
        GROUP BY users.id
    """)
    users_and_task_counts = cur.fetchall()
    print("Users and their task counts:")
    for user, count in users_and_task_counts:
        print("{}: {}".format)
