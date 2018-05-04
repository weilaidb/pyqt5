import pymysql.cursors

databasename = 'python6'
# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    user='root',
    passwd='123456',
    port=3306,
    # db=databasename,
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

try:
  # 执行 SQL 语句
  sql = 'create database if not exists %s' % databasename
  cursor.execute(sql)
  # 提交修改
  connect.commit()
  print("creat database ok,", databasename)
except Exception as e :
    # 发生错误时回滚
    connect.rollback()
    print("create database failed, reason:", e)


connect.select_db(databasename)

try:
  # 执行 SQL 语句
  sql = '''
  CREATE TABLE `trade` (
  `id` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(600) NOT NULL COMMENT '用户真实姓名',
  `account` varchar(1000) NOT NULL COMMENT '银行储蓄账号',
  `saving` decimal(10,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '账户储蓄金额',
  `expend` decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '账户支出总计',
  `income` decimal(8,2) unsigned NOT NULL DEFAULT '0.00' COMMENT '账户收入总计',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
  '''
  # cursor.execute("drop table if exists trade")
  cursor.execute(sql)
  # 提交修改
  connect.commit()
  print("creat table ok")
except Exception as e :
    # 发生错误时回滚
    connect.rollback()
    print("create table failed, reason:", e)


# 插入数据
for i in range(100000):
    try:
        sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
        data = ('世界里' + str(i * 3), '13512345678', 10000 * i)
        cursor.execute(sql % data)
        connect.commit()
        print('成功插入', cursor.rowcount, '条数据, curpos:', i + 1)
    except Exception as e :
        print('失败插入', cursor.rowcount, '条数据, reason:', e, 'curpos', i + 1)

# 修改数据
sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
data = (8888, '13512345678')
cursor.execute(sql % data)
connect.commit()
print('成功修改', cursor.rowcount, '条数据')

# 查询数据
sql = "SELECT name,saving FROM trade WHERE account = '%s' "
data = ('13512345678',)
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("Name:%s\tSaving:%.2f" % row)
print('共查找出', cursor.rowcount, '条数据')

# 删除数据
sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
data = ('13512345678', 1)
cursor.execute(sql % data)
connect.commit()
print('成功删除', cursor.rowcount, '条数据')

# 事务处理
sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "

try:
    cursor.execute(sql_1)  # 储蓄增加1000
    cursor.execute(sql_2)  # 支出增加1000
    cursor.execute(sql_3)  # 收入增加2000
except Exception as e:
    connect.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    connect.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
connect.close()