from typing import Optional,List
from fastapi import Path,Body,FastAPI,Request,Query
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from aioredis import create_redis_pool,Redis
from typing import Dict
import redis
import csv
import uvicorn
import requests

#router=APIRouter()
app=FastAPI()
templates=Jinja2Templates(directory="templates")
class Item(BaseModel):
    name: str
    price: int

class User(BaseModel):
    username:str
    full_name:Optional[str]=None

#根据学号number获取成绩的接口，前端通过/getgrade地址访问
#Query:查询参数  Path:路径  Body:请求体，通过设置le ge None 等值对各个参数进行数值校验

@app.post("/getgrade")
def main(*, item_id: int = Query(..., title="the first query parameter item_id",ge=0,le=100), item: Item, user: User, importance: int = Body(...), q: Optional[str] = None):
    print(item_id)
    print(item)
    print(user)
    print(importance)
    print(q)

    return {"message":"success"}

@app.get("/")
def read_root(request:Request):
    session = requests.Session()
    url = "http://localhost:6375/getgrade/?item_id=5&q='查重报告'"
    #注意传输的json格式数据必须是和函数中的参数同名对应，不仅要数据类对应
    req = session.post(
        url=url,
        json={
            "item":{"name": "haha",
                    "price": 123
                    },
            "user":
                {
                    "username":"dave",
                    "full_name":"Dave Grohl"
                },
            "importance":5
        }
    )
    print(req.text)

    return templates.TemplateResponse(
            "base.html",
            {
                "request":request,
            }
        )

if __name__=='__main__':
    uvicorn.run(app='TestJson:app',host="127.0.0.1",port=6375,reload=True,debug=True)
