#方法名被前后各两个下划线包裹
#__init__:构造函数
#__call__:对象当函数的时候触发
#__str__:当对象被当做字符串时使用
class A():
    def __init__(self):

        print("哈哈哈，我被调用啦")
    def __str__(self):
        return "我被调用啦"
a=A()
print(a)
