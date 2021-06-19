#简历里写的东西都要熟悉; linux 基础命令；版本管理；python 数组 + 加号操作，extend()函数；& 集合操作

#数组+操作
l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)

#数组extend()函数
l3=[1,2,3]
l4=[4,5,6]
l3.extend(l4)
print(l3)
#集合操作
s1={1,5,6}
s2={4,5,6}
s3=s1 & s2

print(s3)
