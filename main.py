from fastapi import FastAPI, HTTPException
from services.user import (
    delete_user
)

app = FastAPI()



@app.delete("/users/{user_id}", response_model=dict)
async def delete_user_endpoint(user_id: int):
    """
    DELETE /users/{user_id}
    Esborra un usuari.
    """
    success = delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuari no trobat")
    return {"deleted": True}




