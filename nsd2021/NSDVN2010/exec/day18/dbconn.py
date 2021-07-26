#!/usr/bin/env python
'''
    创建引擎和连接池
'''
#链接相关
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#操作数据库相关
from sqlalchemy import Column       #变量
from sqlalchemy import Integer      #类
from sqlalchemy import String       #类
from sqlalchemy import ForeignKey   #类
from sqlalchemy import Date         #类

#创建引擎
engine = create_engine(
    #'数据库+操作数据库的模块://用户:密码@数据库地址:端口/默认操作的库?字符集'
    'mysql+pymysql://root:tedu.cn@192.168.214.101/tedu?charset=utf8',
    encoding = 'utf8',  #设置编码字符集
    echo = True     #将sqlalchemy执行的日志打印到屏幕
)
#创建连接池,两个方法
Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.configure(bind=engine)

#生成实体类(表相关)的基类（后边所有的关于操作数据库的表、表记录的类都要以此类作为父类）
Base = declarative_base()

#通过实体类，在库中创建表，如果表已经存在，则不会重新创建

#定义一个部门类，用于实例化部门表
class DepartMents(Base):
    __tablename__ = 'departments'   #指定表名
    dep_id = Column(Integer,primary_key=True)   #指定字段类型
    dep_name = Column(String(20),unique=True)
#定义员工类，用于实例化员工表
class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer,primary_key=True)
    emp_name = Column(String(25))
    email = Column(String(50))
    dep_id = Column(Integer,ForeignKey('departments.dep_id'))
#定义工资类，用于实例化工资表
class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer,primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer,ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)