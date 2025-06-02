from fastapi import FastAPI, HTTPException
from services.user import (
    create_user,
    get_user_by_id,
    update_user,
    delete_user
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



@app.put("/users/{user_id}", response_model=dict)
async def update_user_endpoint(user_id: int, surname: str, street: str):

    updated = update_user(user_id, surname, street)
    if not updated:
        raise HTTPException(status_code=400, detail="No s’ha pogut actualitzar")
    return updated

@app.delete("/users/{user_id}", response_model=dict)
async def delete_user_endpoint(user_id: int):

    success = delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuari no trobat")
    return {"deleted": True}


