#收集参数混合调用顺序：普通参数，*args, g1=v1..,**kvargs
def stu(name,age,*args,hobby="没有",**kwargs):
    print("hellow 大家好")
    print("我叫{0},我今年{1}了，".format(name,age))

    print("我的爱好是{0}".format(hobby))
    print("*"* 10)
    for i in args:
        print(i)
    print("#"*20)
    for k,v in kwargs.items():
        print(k,"...",v)
name="zjx"
age=22
stu(name,age,"zjxx","super",hobby="玩游戏",hobby2="游泳",hobby3="听歌")
