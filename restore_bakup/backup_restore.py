import os
import shutil
from mysql.connector import Error
from connection_pool.connection_pool_study02 import ExplicitlyConnectionPool


class BackupRestore:
    OPTION = """
        CHARACTER SET 'UTF8'
        FIELDS TERMINATED by ','
        LINES TERMINATED by '\r\n'
        """

    def __init__(self, source_dir='C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/', data_dir='data/'):
        self.source_dir = source_dir
        self.data_dir = data_dir

    def data_backup(self, table_name):
        filename = table_name + '.txt'
        try:
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            source_path = self.source_dir + filename
            if os.path.exists(source_path):
                os.remove(source_path)

            backup_sql = "SELECT * FROM {} INTO OUTFILE '{}' {}".format(table_name, source_path, BackupRestore.OPTION)
            cursor.execute(backup_sql)

            if not os.path.exists(self.data_dir):
                os.makedirs(os.path.join('data'))
            shutil.move(source_path, self.data_dir + '/' + filename)  # 파일이 존재하면 overwrite
            print(table_name, "backup complete!")
        except Error as err:
            print(err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def data_restore(self, table_name):
        filename = table_name + '.txt'
        try:
            conn = ExplicitlyConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()

            data_path = os.path.abspath(self.data_dir + filename).replace('\\', '/')
            if not os.path.exists(data_path):
                print("파일 '{}' 이 존재하지 않음".format(data_path))
                return
            restore_sql = "LOAD DATA LOCAL INFILE '{}' INTO TABLE {} {}".format(data_path, table_name, BackupRestore.OPTION)
            cursor.execute(restore_sql)
            conn.commit()
            print(table_name, "restore complete!")
        except Error as err:
            print(err)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
