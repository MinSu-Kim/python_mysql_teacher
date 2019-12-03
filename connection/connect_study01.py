import mysql
from mysql.connector import Error


def connect():  # connect()함수를 사용하여 MySQL 서버에 연결
    """ Connect to MySQL database """

    try:
        # 호스트, 데이터베이스, 사용자 및 비밀번호의 네 가지 매개 변수
        conn = mysql.connector.connect(host="localhost", database="mysql", user="root", password="rootroot")
        # MySQL 데이터베이스에 성공적으로 연결되었는지 확인
        if conn.is_connected():
            print('Connected to MySQL database')
            print(type(conn), conn)
    # MySQL 서버를 사용할 수 없거나 데이터베이스가 없거나 잘못된 사용자 이름 또는 비밀번호와 같은 예외가 발생하면 Python에서 예외가 발생
    except Error as e:
        print(e)

    finally:
        conn.close()  # MySQL Connection의 close()를 사용하여 데이터베이스 연결 종료
        print('Connection closed.')
