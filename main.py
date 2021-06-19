from fastapi import FastAPI,Request,Query

from aioredis import create_redis_pool,Redis

import redis
import csv
import uvicorn

app=FastAPI()

#templates = Jinja2Templates(directory="templates")

def get_csv():
    grade_dict = dict()
    with open("index.csv",'r', encoding='UTF-8') as csv_file:
        grade_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for key,value in enumerate(grade_reader):
            grade_dict[key]=value

    return grade_dict

def get_redis_pool()->Redis:
    r =redis.StrictRedis(host='localhost',port=6379,db=0)
    # await redis.set('aaa', '123')
    # val=await redis.get('aaa', encoding='utf-8')
    grade_dict=get_csv()

    for key, value in grade_dict.items():
        r.set(value[0], value[1])  # 以学生的学号为key，学生的成绩为value
    return r


# async def set_redis(grade_dict):
#     redis = await get_redis_pool()
#     for key, value in grade_dict.items():
#         redis.set(value[0], value[1])  # 以学生的学号为key，学生的成绩为value
#         print(value)
#         # await redis.set('my-key','value')
#     redis.set('aaa','123')
#
#     val_test =redis.get('aaa', encoding='utf-8')
#     print(val_test)
#     val = redis.get('9071246', encoding='utf-8')
#     print(val)

def get_grade(number):
    r = get_redis_pool()
    val =  r.get(number)
    return val



@app.get("/")
def read_root():
    #request=Request()
    grade_dict=get_csv()
    redis=get_redis_pool()
    #set_redis(grade_dict)
    print(get_grade('9017246'))

if __name__=='__main__':
    #request=Request()
    grade_dict=get_csv()
    # print("grade_dict:")
    # print(grade_dict)
    r=get_redis_pool()
    # set_redis(grade_dict)
    print(get_grade('9017246'))
    uvicorn.run(app='main:app',host="127.0.0.1",port=6375,reload=True,debug=True)
