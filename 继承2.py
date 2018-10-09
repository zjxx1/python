class A():
    def __init__(self):
        print("A")
class B(A):
    def __init__(self,name):
        print("B")
        print(name)
class C(B):
    #   C想扩展B的构造函数
    #   即调用B的构造函数后再添加一些功能
    #   有两种方法实现
    #   第一种是通过父类名调用
     def __init__(self,name):
         B.__init__(self,name)
         print("这是C附加的功能")
         # 第二种是使用super调用


     # def __init__(self, name):
     #     super(C,self). __init__(name)
x = C("我是c")