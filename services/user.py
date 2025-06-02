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

def get_user_by_id(user_id: int) -> dict | None:
    conn = config.database.connection_db()
    cursor = conn.cursor()
    try:
        sql = "SELECT id, name, surname, email, course, year, street FROM users WHERE id = %s"
        cursor.execute(sql, (user_id,))
        row = cursor.fetchone()
        return user_schema(row) if row else None
    finally:
        cursor.close()
        conn.close()

def update_user(surname: str, street: str, user_id:int) -> dict:
    conn = config.database.connection_db()
    cursor = conn.cursor()
    try:
        sql = """
            UPDATE users
            SET name = %s, email = %s
            WHERE id = %s
            RETURNING id, name, email
        """
        cursor.execute(sql, (surname, street, user_id))
        updated_row = cursor.fetchone()
        if updated_row:
            conn.commit()
            return user_schema(updated_row)
        else:
            conn.rollback()
            return None
    finally:
        cursor.close()
        conn.close()

