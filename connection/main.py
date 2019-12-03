import inspect

from connection.connect_study01 import connect
from connection.connect_study02 import connect_use_config
from connection.python_mysql_dbconfig import read_db_config


def connect01():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    connect()


def read_config():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    db = read_db_config()
    print(type(db), " : ", db)


def connect02():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    connect_use_config()


if __name__ == '__main__':
    connect01()
    connect01()
    # read_config()
    connect02()
    connect02()

    # connect_use_config()
    # connect_use_config()
    # connection_pool01()
    # connection_pool01()




# def connection_pool01():
#     connection = DatabaseConnectionPool.get_instance().get_connection()
#     print(type(connection), connection)
#     cursor = connection.cursor()
#     cursor.execute("select * from product")
#     rows = cursor.fetchall()
#     print('Total Row(s):', cursor.rowcount)
#     for row in rows:
#         print(type(row), " => ", row)
#     connection.close()
