import subprocess
import sys

# Package list
packages = ['nginx', 'python3', 'python3-pip']

# Install packages
for package in packages:
    result = subprocess.run(["apt-get", "install", "-y", package])
    if result.returncode == 0:
        print("Package installed successfully:", package)
    else:
        sys.exit("Failed to install package:", package)
