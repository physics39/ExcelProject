import redis

r=redis.Redis(host='localhost',port=6379,decode_responses=True)#decode_reponses=True,redis默认取出来的结果是字节，可以改为字符串
r.set('name','runoob')#设置name对应的值为runoob

print(r['name'])#用name作为key取出value:runoob
print(r.get('name'))
print(type(r.get('name')))

d={'k1':'v1','k2':'v2'}
r.mset(d)
print(r.mget("k1","k2"))#直接传入字典

#切片操作
r.set("name","Southeast University")
print(r.getrange("name",0,2))#取前三个字符的切片
print(r.getrange("name",0,-1))#取所有的字节


pool=redis.Connection(host='localhost',port=6379,decode_responses=True)

#问题：怎么使得多个redis实例共享一个连接池？