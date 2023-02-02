import subprocess
import sys

username = input("Enter username: ")
password = input("Enter password: ")

# Create user
result = subprocess.run(["useradd", "-m", "-p", password, username])
if result.returncode == 0:
    print("User created successfully")
else:
    sys.exit("Failed to create user")

# Add user to sudoers
with open("/etc/sudoers", "a") as f:
    f.write(username + " ALL=(ALL) NOPASSWD:ALL\n")
print("User added to sudoers")
