# coding: utf8

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:redhat@127.0.0.1:3306/test')

# 创建表
insert_table_user = """ create table user (id int, name varchar(80), salary int not null) """
engine.execute(insert_table_user)

# 插入数据
sql1 = """ insert into user(id ,name, salary) values (1,'zs',9999)"""
engine.execute(sql1)

# 查询数据
sql2 = """ select * from user """
result = engine.execute(sql2)
print(result.fetchall())