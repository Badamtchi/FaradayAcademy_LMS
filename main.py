from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title='Fast API LMS',
    description='LMS for managing students and courses',
    version='0.0.1',
    contact={
        'name': 'Mehrdad',
        'email': 'mehrdad@gentleman.com'
    },
    license_info={
        'name': 'BCE'
    }
)



users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get('/users', response_model=List[User])
async def get_user():
    return users

@app.post('/users')
async def creat_user(user: User):
    users.append(user)
    return "Success"

@app.get('/users/{id}')
async def get_user(
    id:int = Path(..., description='The ID of the user you want to retrieve.', gt=2),
    is_active: str = Query(None, max_length=5)
    ):
    return { "user": users[id], "query":q }