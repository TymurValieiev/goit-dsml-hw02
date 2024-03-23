from faker import Faker
import psycopg2

def populate_database(num_users, num_tasks_per_user):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="mysecretpassword",
        host="localhost"
    )
    cur = conn.cursor()

    fake = Faker()

    for _ in range(num_users):
        fullname = fake.name()
        email = fake.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
        conn.commit()

    statuses = ['new', 'in progress', 'completed']
    for status in statuses:
        cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))
        conn.commit()

    cur.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cur.fetchall()]
    for user_id in user_ids:
        for _ in range(num_tasks_per_user):
            title = fake.sentence()
            description = fake.text()
            status_id = fake.random_int(min=1, max=len(statuses))
            cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                        (title, description, status_id, user_id))
            conn.commit()

    cur.close()
    conn.close()

if __name__ == "__main__":
    populate_database(10, 5)