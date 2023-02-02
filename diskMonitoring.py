import subprocess
import sys

# Threshold for disk space usage in percentage
threshold = 90

# Get disk space usage
result = subprocess.run(["df", "-h"], stdout=subprocess.PIPE)
output = result.stdout.decode("utf-8").split("\n")

# Check disk space usage
for line in output:
    if "%" in line:
        split_line = line.split()
        if int(split_line[4][:-1]) > threshold:
            sys.exit("Disk space usage exceeded threshold:", split_line[0])

print("Disk space usage within threshold")
