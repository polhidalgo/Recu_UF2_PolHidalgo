import config.database
from schemas.user_sch import users_schema, user_schema


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

