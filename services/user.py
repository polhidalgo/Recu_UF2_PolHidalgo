import config.database


def delete_user(user_id: int) -> bool:
    conn = config.database.connection_db()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM users WHERE id = %s RETURNING id"
        cursor.execute(sql, (user_id,))
        deleted = cursor.fetchone()
        if deleted:
            conn.commit()
            return True
        else:
            conn.rollback()
            return False
    finally:
        cursor.close()
        conn.close()