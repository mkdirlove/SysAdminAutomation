import subprocess
import sys
import time

# Database name
db_name = input("Enter database name: ")

# Backup destination
dst_dir = '/backup'

# Database backup
timestamp = time.strftime('%Y%m%d%H%M%S')
dst_file = dst_dir + '/' + db_name + '_' + timestamp + '.sql'
result = subprocess.run(["mysqldump", "-u", "root", "-p", db_name, "--result-file=" + dst_file])
if result.returncode == 0:
    print("Database backup successful:", dst_file)
else:
    sys.exit("Failed to backup database:", dst_file)
