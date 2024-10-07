from fastapi import APIRouter
# runModel2도 불러와주자.
from src.services.model import runModel, runModel2
# dtos/house.py 경로에서 정의한 Body 타입을 가진 class를 불러온다.
from src.dtos.house import GetPredictionOfHousePrice2BodyDto

house_router = router = APIRouter()


@router.get("/price/predict")
async def getPredictionOfHousePrice(crim: float, room: float):
  price = await runModel(crim, room)
    
  return price

# 추가된 코드. post 요청으로 model을 돌린다.
@router.post("/price/predict")
# body인자로 아까 만들었던 Dto class를 설정해준다.
async def getPredictionOfHousePrice2(body: GetPredictionOfHousePrice2BodyDto):
  price = await runModel2(body)
  
  return price