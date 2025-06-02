
def user_schema(user) -> dict:
    response = {
        "id":user[0],
        "name":user[1],
        "surname":user[2],
        "email":user[3],
        "description":user[4],
        "course":user[5],
        "year":user[6],
        "street":user[7],
        "postal_code":user[8],
        "password":user[9],
    }
    return response

def users_schema(users) -> list[dict]:
    response = [user_schema(user) for user in users]
    return response

