from fastapi import FastAPI, HTTPException
from services.user import (
    create_user,
    get_user_by_id
)

app = FastAPI()


@app.post("/users", response_model=dict)
async def create_user_endpoint(
    name: str, email: str, surname: str, description: str, course: str, year: int, street: str, postal_code: int, password: str
):
    new_user = create_user(name, email, surname, description, course, year, street, postal_code, password)
    return new_user

@app.get("/users/{user_id}", response_model=dict)
async def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuari no trobat")
    return user


