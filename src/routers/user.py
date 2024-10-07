# user.py
from fastapi import APIRouter
from pydantic import BaseModel

user_router = router = APIRouter()

# Body의 타입을 정의한다.
class CreatePostBodyDto(BaseModel):
  name: str
  age: int
  height: int
  

@router.post("/")
async def createUser(body: CreatePostBodyDto):
  
  name = body.name
  age = body.age
  height = body.height
  
  processed_age = f"{age}살"
  processed_height = f"{height}cm"
  
  return {"name": name, "age": processed_age, "height": processed_height}