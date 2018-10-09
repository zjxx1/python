class Teacher():
    name="zgx"
    age=22

    def __init__(self):
        self.name="zjx"
        self.age=19
    def say(self,name,age):
        print("my name is {0}".format(self.name))
        print(("my age is {0}".format(self.age)))
    def sayAgain():
        print(__class__.name)#访问类中的成员变量
        print(__class__.age)#访问类中的成员变量
        print("hellow,nice to meet you again")
    def say3(a):
        print(a.name)
        print(a.age)

z= Teacher ()
z.say("jjj",25)
Teacher.sayAgain()
Teacher.say3(z)
z.say3()

