#模块名称以数字开头，则借助importlib帮助
#语法
   #import importlib
   #相当于导入了一个叫02的模块并把导入模块赋值给了zj
   #zj=importlib.import_module("02")
   #zjx=zj.student()
   #zjx.类中的方法()

   # import module_name  *
   #zjx=module_name.导入的类名()
    #zjx.类中的方法()



  #import 模块 as 别名   *



  #if__name__=='__main__'
  #可以有效避免模块导入时候被动执行的问题，
  # 建议所有程序的入口都以此代码为入口


