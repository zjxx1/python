# 声明一个类并且指定当前类的元类
class x(metaclass=abc.ABCMeta):

    #定义一个抽象的方法
    @abc.abstractmethod
    def x(self):
        pass
    #定义类抽象方法
    @abc.abstractclassmethod
    def x(self):
        pass
    #定义静态抽象方法
    @abc.abstractstaticmethod
    def x(self):
        pass