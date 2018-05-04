import pymysql

try:
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306)
    cur = conn.cursor()

    cur.execute('create database if not exists python')
    conn.select_db('python')
    cur.execute('create table test(id int,info varchar(20))')

    value = [1, 'hi rollen']
    cur.execute('insert into test values(%s,%s)', value)

    values = []
    for i in range(20):
        values.append((i, 'hi rollen' + str(i)))

    cur.executemany('insert into test values(%s,%s)', values)

    cur.execute('update test set info="I am rollen" where id=3')

    conn.commit()
    cur.close()
    conn.close()

except (pymysql.Error):
    print("pymysql error")
    # print("Mysql Error %d: %s" % (e.args[0], e.args[1]))