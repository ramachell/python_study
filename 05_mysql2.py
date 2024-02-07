import pymysql

# MySQL 연결 정보
host = "localhost"
user = "root"
password = "password"
database = "pythonS"

# MySQL에 연결
connection = pymysql.connect(host=host,
                             port=23306,
                             user=user,
                             password=password,
                             database = database
)

# try:
#     with connection.cursor() as cursor:
#         # 쿼리 실행
#         sql = "SELECT * FROM student"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)

    
#     with connection.cursor() as cursor:
#         sql = "insert into student values(4,'kim','M')"
#         cursor.execute(sql)
        

# finally:
#     connection.close()

try:
    with connection.cursor() as cursor:
        # 쿼리 실행
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

    # with connection.cursor() as cursor:
    #     sql = "INSERT INTO student VALUES (4, 'kim', 'M')"
    #     cursor.execute(sql)
    #     connection.commit()
            
finally:
    connection.close()


def del_id(id):
    connection = pymysql.connect(host=host,
                             port=23306,
                             user=user,
                             password=password,
                             database = database
)
    
    try:
        with connection.cursor() as cursor:
            sql = f"delete from student where id = {id}"
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()

del_id(4)