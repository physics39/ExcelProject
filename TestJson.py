from typing import Optional,List
from fastapi import FastAPI,Request,Query
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from aioredis import create_redis_pool,Redis
from typing import Dict
import redis
import csv
import uvicorn

#router=APIRouter()
app=FastAPI()
templates=Jinja2Templates(directory="templates")
class Item(BaseModel):
    name: str
    price: int

#根据学号number获取成绩的接口，前端通过/getgrade地址访问
@app.post("/getgrade")
def main(q:Item):
    # print(item_id)
    print(q)
    return {"message":"success"}

@app.get("/")
def read_root(request:Request):
  return templates.TemplateResponse(
        "base.html",
        {
            "request":request,
        }
    )

if __name__=='__main__':
    #print(get_grade('9017246'))#调用获取成绩的接口,得到对应成绩
    uvicorn.run(app='TestJson:app',host="127.0.0.1",port=6375,reload=True,debug=True)
