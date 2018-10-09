#property 当前类中使用，可以控制一个类中的多个属性(人为地增加一些功能）
#property的四个参数（fget（可以任意参数），fset，fdel，“例子”）
#第一个参数代表读取的时候需要调用的函数
#第二个参数代表写入的时候需要调用的函数
#第三个是删除
class B():
    def __init__(self):
        self.name="hah"
        self.age=18
    def fget(self):

        return self.name *2
    def fset(self,name):
        self.name= name.upper()#该函数用于对字母全大写
        print("我是 {0}".format(self.name))
    n=property(fget,fset)#添加了这两个功能
a=B()
a.n="zjxxx1"
print(a.n)
#__dict__:以字典的方式显示类的成员组成  B.__dict__
#__doc__:获取类的文档信息
#__name__:获取类的名称，如果在模块中使用，获取模块的名称
#__bases__:获取某个类的所有父类，以元组的方式显示


