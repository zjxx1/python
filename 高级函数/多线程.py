#threading（包）的使用
#1. t= threading.Thread(target.函数，args=(参数，)
#2. start():启动多线程
import  time
import  threading
def fun():

    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1=threading.Thread(target=fun,args=())
t1.start()
print("super zjxx")

time.sleep(1)
print("Main thread end")