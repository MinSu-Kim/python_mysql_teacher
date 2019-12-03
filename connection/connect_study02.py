from mysql.connector import MySQLConnection, Error
from connection.python_mysql_dbconfig import read_db_config


def connect_use_config():
    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)  # 매개변수가 dictionary 자료구조

        if conn.is_connected():
            print('connection established.')
            print(type(conn), conn)
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')
