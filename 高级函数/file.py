#with函数
#第一个参数：必须有，文件的路径和名称
#r表示后面字符串内容不需要转义
with open(r"文件路径\xx.txt","w") as z:
    #按行读取内容
   zjx=z.readline()
    #此结构能够保证完整读取文件直到结束
   while zjx:
       print(zjx)
       zjx=z.readline()
#文件写的操作-write
#向文件追加一句诗
#a代表追加
print("*"*20)
with open(r"文件路径\xx.txt",'a') as f:
    f.write("生活不仅有眼前的苟且， \n 还有远方的苟且")
#pickle
#序列化（持久化，落地）：把程序运行中的信息保存在磁盘上
# pickle.dump:序列化(执行写的操作）
# pickle.load:反序列化(执行读的操作）
print("*"*20)
import pickle
a=["19","zjxxx","I love running"]
with open(r"文件路径\xx.txt","wb") as x:
    pickle.dump(a,x)

with open(r"文件路径\xx.txt","rb") as x:
    c=pickle.load(a,x)
    print(c)

