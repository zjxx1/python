# 创建Student类，描述学生类
# 学生具有Student。name属性
# 但name格式并不统一
# 可以增加一个函数，然后自动调用的方式
class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.setName(name)
        #介绍下自己
    def intro(self):
            print("Hi,my name is {0}".format(self.name))
       #例如名字全部大写
    def setName(self,name):
        self.name=name.upper()
s1=Student("Zhoujixiao",22)
s2=Student("zjxx",21)

s1.intro()
s2.intro()