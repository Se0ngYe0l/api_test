from pydantic import BaseModel

class GetPredictionOfHousePrice2BodyDto(BaseModel):
  crim: float
  zn: float
  indus: float
  chas: int
  nox: float
  room: float
  age: float
  dis: float
  rad: int
  tax: float
  ptratio: float
  b: float
  lstat: float