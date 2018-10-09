class Animel():
    def __init__(self):
        print("我是一只动物呀")
class Bird(Animel):
    def __init__(self,name):
        self.name=name
        print("我是一只小小鸟{0}".format(name))
class jinsique(Bird):
     pass

z=jinsique("xiaoxiaoniao")

