import psycopg2

def create_tables():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="mysecretpassword",
        host="localhost"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(100),
            email VARCHAR(100) UNIQUE
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS status (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            description TEXT,
            status_id INTEGER REFERENCES status(id),
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
