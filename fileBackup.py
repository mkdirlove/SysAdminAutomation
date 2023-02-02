import shutil
import sys
import time

# Source file
src_file = input("Enter source file path: ")

# Backup destination
dst_dir = '/backup'

# File backup
timestamp = time.strftime('%Y%m%d%H%M%S')
dst_file = dst_dir + '/' + os.path.basename(src_file) + '_' + timestamp
shutil.copy2(src_file, dst_file)
print("File backup successful:", dst_file)
