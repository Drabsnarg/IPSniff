import os
from pathlib import Path

# Define the target directories for the search
target_directories = ["C:\\", "E:\\"]

# Get the path to the user's desktop
desktop_path = Path.home() / "Desktop"

# Define the output file path
output_file_path = 'C:\\Users\\cdreh\\OneDrive\\Documents' "jar_files.txt"

# Function to recursively search for .jar files and write their names to the output file
def find_jar_files(directory, output_file):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jar"):
                jar_file_path = os.path.join(root, file)
                output_file.write(jar_file_path + "\n")

# Open the output file in write mode
with open(output_file_path, "w") as output_file:
    # Iterate through each target directory
    for directory in target_directories:
        # Call the function to search for .jar files and write their names
        find_jar_files(directory, output_file)

print("Jar file names written to", output_file_path)
