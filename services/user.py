import config.database
from schemas.user_sch import users_schema, user_schema


def create_user(name: str, email: str, surname: str, description: str, course: str, year: int, street: str, postal_code: int, password: str) -> dict:
    conn = config.database.connection_db()
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO users (name, surname, email, description, course, year, street, postal_code, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id, name, email"
        cursor.execute(sql, (name, surname, email, description, course, year, street, postal_code, password))
        new_row = cursor.fetchone()
        conn.commit()
        return user_schema(new_row)
    finally:
        cursor.close()
        conn.close()

