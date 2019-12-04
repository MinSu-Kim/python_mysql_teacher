from restore_bakup.backup_restore import BackupRestore
import platform

from restore_bakup.backup_restore2 import BackupRestore2

if __name__ == "__main__":
    backup_restore = BackupRestore()
    # backup_restore.data_backup('product')
    # backup_restore.data_backup('sale')
    backup_restore.data_restore('product')
    backup_restore.data_restore('sale')
    print(platform.platform().split('-')[0])