import os
import subprocess

# Define the target directory for the search
target_directory = "C:\\"

# Define the file name to search for
file_to_find = "client.jar"

# Function to recursively search for the file and return its path
def find_file(directory, file_name):
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

# Search for the file in the target directory
file_path = find_file(target_directory, file_to_find)

if file_path:
    # Open the file in Visual Studio Code
    subprocess.run(["code", file_path])
    print("File opened in Visual Studio Code.")
else:
    print("File not found in the specified directory.")
