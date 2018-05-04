import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mysql') #这里写上面设置的密码
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
row = cursor.fetchone()
print("MySQL server version:", row[0])
cursor.close()
conn.close()