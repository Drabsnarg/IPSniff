import os
import shutil
import datetime
import zipfile

# Get today's date
today = datetime.date.today().strftime("%Y-%m-%d")

# Create a new folder with today's date
new_folder = os.path.join("D:", "DCIM", today)
os.makedirs(new_folder, exist_ok=True)

# Get the list of files in the source folder
source_folder = os.path.join("D:", "DCIM", "100OLYMP")
files = os.listdir(source_folder)

# Move files to the new folder with unique names
for file in files:
    source_file = os.path.join(source_folder, file)
    dest_file = os.path.join(new_folder, f"{today}_{file}")
    shutil.move(source_file, dest_file)

# Compress the moved files into a zip archive
archive_name = os.path.join("E:", f"{today}_Archive.zip")
with zipfile.ZipFile(archive_name, "w") as zipf:
    for file in os.listdir(new_folder):
        file_path = os.path.join(new_folder, file)
        zipf.write(file_path, file)

# Clean up the new folder (optional)
shutil.rmtree(new_folder)

print("Files moved and compressed successfully!")
