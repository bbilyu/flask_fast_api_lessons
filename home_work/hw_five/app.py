from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel


app = FastAPI()



class User(BaseModel):
    id: int
    name: str
    status: str

users = []

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.get("/users/{id}", response_model=User)
async def get_user(id: int):
    for user in users:
        if user.get('id') == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users", status_code=201)
async def add_user(user: User):
    users.append(user.dict())
    return {"message": "User created"}

@app.put("/users/{id}", status_code=200)
async def update_user(id: int, user: User):
    for index, existing_user in enumerate(users):
        if existing_user.get('id') == id:
            users[index] = user.dict()
            return {"message": "User updated"}
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{id}", status_code=200)
async def delete_user(id: int):
    for index, user in enumerate(users):
        if user.get('id') == id:
            users.pop(index)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")