from fastapi import FastAPI, HTTPException
from services.user import (
    create_user,
    get_user_by_id
)

app = FastAPI()


@app.get("/users/{user_id}", response_model=dict)
async def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuari no trobat")
    return user


