from fastapi import FastAPI, HTTPException
from services.user import (
    update_user
)

app = FastAPI()


@app.put("/users/{user_id}", response_model=dict)
async def update_user_endpoint(user_id: int, name: str, email: str):

    updated = update_user(user_id, name, email)
    if not updated:
        raise HTTPException(status_code=400, detail="No s’ha pogut actualitzar")
    return updated


