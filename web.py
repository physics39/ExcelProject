from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from aioredis import create_redis_pool,Redis
from typing import Dict,List
import redis
import csv
import uvicorn

#router=APIRouter()
app=FastAPI()
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True, db=0)  # redis server的IP地址和端口号为：localhost:6379，访问第0个数据库db
templates=Jinja2Templates(directory="templates")
def get_csv():
    grade_dict = dict()
    with open("index.csv",'r', encoding='UTF-8') as csv_file:#从本地读取csv格式的文件
        grade_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for key,value in enumerate(grade_reader):
            grade_dict[key]=value

    return grade_dict

def set_grade():

    grade_dict=get_csv()

    for key, value in grade_dict.items():
        r.set(value[0], value[1])  # 以学生的学号为key 9017246，学生的成绩为value 245，文件中的内容为(9017246,245)
    return r

#根据学号number获取成绩的接口，前端通过/getgrade地址访问
@app.get("/getgrade/")
def get_grade(number:str):
    print("成功调用get_grade")
    val = r.get(number)
    print(val)
    return val

@app.get("/")
def read_root(request:Request):
    grade_dict=get_csv()
    redis=set_grade()
    #grade=get_grade('9017246')
    return templates.TemplateResponse(
        "index.html",
        {
            "request":request,
        }
    )

if __name__=='__main__':
    #print(get_grade('9017246'))#调用获取成绩的接口,得到对应成绩
    uvicorn.run(app='web:app',host="127.0.0.1",port=6375,reload=True,debug=True)
