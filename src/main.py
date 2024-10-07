# main.py
from fastapi import FastAPI
from src.routers.index import index_router

app = FastAPI(docs_url="/docs", openapi_url="/open-api-docs")

# /api라는 경로로 index_router를 붙인다.
app.include_router(index_router, prefix="/api")

# / 라는 url로 GET 요청이 들어오면 getHello함수를 실행시키겠다.  
@app.get("/")
async def getHello():
  return "Hello, World"