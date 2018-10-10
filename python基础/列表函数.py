#append 插入一个内容，在末尾追加
a=[i for i in range(1,5)]

a.append(100)
print(a)
#insert 指定位置插入
a=[i for i in range(1,5)]

a.insert(3,200)
print(a)
#  remove删除 移除列表内指定的值
a=[i for i in range(1,5)]

a.remove(4)
print(a)
#reverse 翻转列表内容，原地翻转
a=[i for i in range(1,5)]

a.reverse()
print(a)
#extend 扩展列表，两个列表，把一个直接拼到后一个
a=[i for i in range(1,5)]
b=[i for i in range(5,10)]
a.extend(b)
print(a)
#count 查找列表中指定值或元素的个数
a=[i for i in range(1,11)]
a.append(10)
a.insert(2,10)
x=a.count(10)
print(x)
#copy (浅拷贝）拷贝要改变地址 ，赋值不会改变地址
a=[i for i in range(1,5)]
print(id(a))
b=a
print(id(b))
print("*"*20)
a=[i for i in range(1,5)]
print(id(a))
b=a.copy()
print(id(b))

s={1,2,3,4}
print(type(s))
print(s)