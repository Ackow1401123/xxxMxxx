from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class UserInfo(BaseModel):
    name: str
    email: str
    age: int | None = None

users: List[UserInfo] = []

@app.post("/webhook")
async def receive_user_info(user: UserInfo):
    users.append(user)
    return {"status": "received", "total_users": len(users)}

@app.get("/users")
async def get_users():
    return users
