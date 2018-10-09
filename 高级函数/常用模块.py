#calendar
#跟日历相关的模块
print("*"*20)
#time模块（重点）
###时间戳 ：一个时间表示，是从1970年1月1日0时0分0秒到现在经历的秒数
import time
#得到时间戳
time.time()
t=time.localtime()
#sleep:使程序进入睡眠，n秒后继续
for i in range(10):
    print(i)
    time.sleep(0.5)#执行时间间隔为0.5秒
#clock:获取程序执行的时间
print("*"*20)
#datetime 模块
import datetime
#datetime。date提供一个理想和的日期。
dt=datetime.date(2018,9,30)
print(dt)
#os -操作系统相关
# os  操作系统目录相关
# os.path ,系统路径相关
# getcwd() 获取当前的工作目录
#chdir() 改变当前的工作目录
import os
os.chdir("所在路径")
x=os.getdir()
print(x)
#listdir()获取一个目录中所有子目录和文件的名称列表

print("*"*20)
#random
#random() 获取0-1之间的随机小数
#格式： random.random()
import random
print(random.random())
print(random.randrange(0,100))