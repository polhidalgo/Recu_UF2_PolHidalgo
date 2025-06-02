from fastapi import FastAPI
from typing import List
from services.user import (
    create_user
)

app = FastAPI()


@app.post("/users", response_model=dict)
async def create_user_endpoint(
    name: str, email: str, surname: str, description: str, course: str, year: int, street: str, postal_code: int, password: str
):
    new_user = create_user(name, email, surname, description, course, year, street, postal_code, password)
    return new_user



