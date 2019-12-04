from database_setting.db_connection.coffee_init_service import DBInitService
from database_setting.db_connection.read_ddl import read_ddl_file


def read_ddl_file_test():
    db = read_ddl_file()
    print(db)
    for key, value in db.items():
        if key != 'sql':
            print("[{}] = {}".format(key, value))
        else:
            print("[{}]".format(key))
            for k, v in value.items():
                print("\t[{}]\n\t\t{}".format(k, v))


if __name__ == "__main__":
    # read_ddl_file_test()
    db = DBInitService()
    db.service()
    db.data_restore("product")
    db.data_restore("sale")
    # db.data_backup("product")
    # db.data_backup("sale")