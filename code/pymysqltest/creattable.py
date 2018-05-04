import pymysql

# 打开数据库 （如果连接失败会报错）
# db = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'minbo', passwd = '123456', db = 'pythontest')
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='pythontest', charset="utf8")

# 获取游标对象
cursor = db.cursor()

# 执行sql查询操作
sql_select = "select version()"
cursor.execute(sql_select)

# 使用fetchone()获取单条数据
data = cursor.fetchone()
print("DB version is : %s" % data)

# #创建数据库pythontest
# cursor.execute("drop database if exists pythontest")  #如果数据库已经存在，那么删除后重新创建
# sql = "create database pythontest;"
# cursor.execute(sql)


# 如果user表存在，就删除
cursor.execute("drop table if exists user")

# 创建表user
sql_create = "create table user(id int, name varchar(10)) engine = innodb charset = utf8"
cursor.execute(sql_create)

# 插入操作
sql_insert = '''insert into user(id, name) values (2, "李明")'''
try:
    # 执行sql
    cursor.execute(sql_insert)
    db.commit()
except:
    # 发生异常
    db.rollback()

# 查询操作
sql_select = '''select * from user'''
try:
    # 执行sql语句
    cursor.execute(sql_select)
    # 获取所有记录列表
    result = cursor.fetchall()
    for row in result:
        id = row[0]
        name = row[1]
        print("id = %d, name = %s" % (id, name))
except:
    print("Error: unable to fecth data")

# 执行事务
'''事务机制可以确保数据的一致性  
    1.事务有四个属性：原子，一致，隔离，持久；通常称为ACID  
    2.Python DB API2.0的事务提供了两个方法：commit 和 rollback  
    3.对于支持事务的数据库，在python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务，  
    这个区别于mysql客户端，commit()方法提交所有的事务，rollback()方法回滚当前游标的所有操作。每个方法都开启了一个新的事务'''
# 例子
sql_insert = '''insert into test(id, name) values (1, 'china')'''
try:
    cursor.execute(sql_insert)
    db.commit()
except:
    db.rollback()

print("end")
# 关闭连接
db.close()