#把函数作为参数使用的函数，叫高阶函数
a=100
b=a
def funA():
    print("aaaa")
funB=funA
funB()
print("*"*20)
#既然函数名称是变量，则应该可以被当做参数传入另一个函数
#假如funC是普通函数，返回一个传入数字的100倍数字
def funC(n):
    return  n*100
#再写一个函数，把传入参数乘以300倍
def funD(n):
    return funC(n)*3
print(funD(9))
print("...."*4)
def funE(n,f):
    return f(n)*3
print(funE(9,funC))
print("*"*20)
#系统的高阶函数-map
#有一个列表，想对列表里的每个元素乘以10，获得一个新的#列表
list1=[1,3,1,8,2,7]
print(list1)
list2=[]
list2.append(list1*10)
print(list2)
#利用map实现
def x(n):
    return n*10
list3=map(x,list1)

list4=[i for i in list3]
print(list4)
print("*"*20)
#reduce
#把一个可迭代对象最后归并成一个结果
#必需有两个参数，必须有返回值
from functools import reduce
def xy(x,y):
    return x+y
zjx=reduce(xy,[1,2,3,4,5,6])
print(zjx)
print("*"*20)
#高阶函数-排序
# 把一个序列按照给定算法进行排序
# key：在排序前对每一个元素进行key函数运算，可以理解成按照key函数定义的逻辑进行排
a=[-21,1,85,116,48,-6662,8]
al=sorted(a,reverse=True)#对函数进行从大到小排序
print(al)
#abs是求绝对值的意思
ax=sorted(a,key=abs,reverse=False)
print(ax)
print("*"*20)
#装饰器    ***
#在不改动函数代码的基础上无限制扩展函数功能的一种机制，本质上讲，装饰器是一个返回函数的高阶函数
#装饰器的使用：使用@语法，即在每次要扩展到函数定义前使用@+函数名
import time
#j是被装饰的函数作为了参数（高阶函数）
def printTime(j):
    def zjx(*args,**kwargs):
        print("Time:",time.ctime())
        return j(*args,**kwargs)
    return zjx
@printTime
def hello():
    print("Hello world")
hello()
print("*"*20)
#zip
#把两个可迭代内容生成一个可迭代的tuple类型组成的内容
x1=["zjx","yk","zgx","rzy"]
x2=[80,81,85,86]
x3=zip(x1,x2)
x4=[i for i in x3]
print(x4)