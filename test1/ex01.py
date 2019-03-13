#coding: utf8

# 引入模块
import pymysql.cursors

# 获取数据库链接
connection = pymysql.connect(host='172.18.97.85',
                    user='root',
                    password='Bmw@123///',
                    db='test1',
                    charset='utf8mb4')


# 获取会话指针
cur = connection.cursor()

# 执行 SQL 语句
cur.execute(sql)
