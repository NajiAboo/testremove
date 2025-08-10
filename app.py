from fastapi import FastAPI
from pydantic import BaseModel

class user(BaseModel):
    name: str
    age: int

app = FastAPI()


user_data = {
    1: {"name": "naji", "age": 10}
}


@app.get("/users")
def get_user():
    return user_data


@app.put("/user/{user_id}")
def update_user(user_id: int, update_Data: user):
    print(f"userid  : {user_id}")

    if user_id in user_data:
        user_data[user_id] = update_Data.model_dump()
        return {"message": "upddaed sucessfuly"}
    return {"message": "failed"}
    

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id in user_data:
        del user_data[user_id]
        return {"message": "sucessfully deleted"}


