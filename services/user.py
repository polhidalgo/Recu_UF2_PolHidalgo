import config.database
from schemas.user_sch import users_schema, user_schema

def update_user(user_id: int, surname: str, street: str) -> dict | None:
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
