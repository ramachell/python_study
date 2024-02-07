import pymysql

connection = pymysql.connect(host = 'localhost:23306',
                             user='user',
                             password='password',
                             database='pythonS',
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        sql = "insert into `student` (`id`,`name`,`gender`) values (%s,%s)"
        cursor.execute(sql,('1','coddde','M'))

        connection.commit()

    with connection.cursor() as cursor:
        sql = "select * from `student` where `gender` = %s"
        cursor.execute(sql,'M')
        result = cursor.fetchall()
        print(result)