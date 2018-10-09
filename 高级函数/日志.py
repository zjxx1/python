#写日志实例需要制定级别，只有当级别等于或高于指定级别才被记录
#使用下列函数：
#logging.debug(msg,*args,**kwargs) 创造一条严重级别为DEBUG的日志文件
#logging.info(msg,*args,**kwargs) 创造一条严重级别为INFO的日志文件
#logging.warning(msg,*args,**kwargs) 创造一条严重级别为WARNING的日志文件
#logging.error(msg,*args,**kwargs) 创造一条严重级别为EROOR的日志文件


#logging.basicConfig(**kwargs) 对root logger进行一次性配置
#只在第一次调用的时候起作用(修改文件的严重级别）
#logging.basicConfig( "文件目录",level=logging.级别)
import logging
logging.basicConfig(filename="文件目录",level=logging.debug)
logging.debug("This is a debug log")
logging.info("This is a debug info")
logging.warning("This is a warning log")
logging.error("This is a error log")

#logger 日志器  产生一个日志
# Logger.setlevel()设置日志器将会处理的日志消息最低严重级别
#Logger.debug()产生一条debug级别的日志

#如何得到一条日志
#logger.getlogger()

#handler 处理器  把产生的日志发送到相应的目的地
#方法：logger.addfileter() logger.removeFileter()
#不需要直接使用，是被其他类继承（基类）