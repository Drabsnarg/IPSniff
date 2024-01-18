import csv
import os
import shutil
import hashlib
import logging
import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
from PIL import Image, ImageTk  # Import PIL for image handling

# Set up logging
logging.basicConfig(filename='file_operations.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to generate MD5 hash for a file
def generate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Function to write failed files to a CSV file with a counter
def write_failed_files_to_csv(failed_files):
    counter = 1
    while os.path.exists(f"failed_{counter}.csv"):
        counter += 1
    with open(f"failed_{counter}.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for filename in failed_files:
            writer.writerow([filename])

# Functions to browse for directories and files
def browse_csv():
    filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    csv_entry.delete(0, tk.END)
    csv_entry.insert(0, filename)

def browse_directory(entry_widget):
    folder_selected = filedialog.askdirectory()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, folder_selected)

# Function to perform file operations
def perform_operations():
    operation = operation_var.get()
    src_dir = src_entry.get()
    dest_dir = dest_entry.get()
    csv_path = csv_entry.get()

    failed_files = []

    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            filename = row[0].strip()
            src_path = os.path.join(src_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            
            try:
                src_md5 = generate_md5(src_path)
                if operation == 'Copy':
                    shutil.copy(src_path, dest_path)
                elif operation == 'Move':
                    shutil.move(src_path, dest_path)
                dest_md5 = generate_md5(dest_path)

                if src_md5 == dest_md5:
                    message = f"Successfully performed {operation} on {filename}"
                    checksum_message = f"MD5 checksum validation successful for {filename}"
                    logging.info(checksum_message)  # Logging the success of checksum validation
                else:
                    message = f"MD5 hash mismatch after {operation} on {filename}"
                    failed_files.append(filename)
                
                status_text.insert(tk.END, f"{message}\n")
                logging.info(message)

            except Exception as e:
                message = f"Failed to perform {operation} on {filename}: {e}"
                status_text.insert(tk.END, f"{message}\n")
                logging.error(message)
                failed_files.append(filename)
    
    if failed_files:
        write_failed_files_to_csv(failed_files)
        message = f"Failed to perform {operation} on the following files: {', '.join(failed_files)}"
        status_text.insert(tk.END, f"{message}\n")
        logging.error(message)
    else:
        message = f"All files {operation.lower()}ed successfully."
        status_text.insert(tk.END, f"{message}\n")
        logging.info(message)

# Initialize Tkinter window
root = tk.Tk()
root.title("File Operations Utility")

## Add a logo using PIL
#image = Image.open("logo.png")  # Replace with your logo's file path
#photo = ImageTk.PhotoImage(image)
#logo_label = tk.Label(root, image=photo, bg='lightblue')
#logo_label.pack()

# Create entry widgets for source and destination directories
src_label = tk.Label(root, text="Source Directory:")
src_label.pack()
src_entry = tk.Entry(root, width=50)
src_entry.pack()
src_button = ttk.Button(root, text="Browse", command=lambda: browse_directory(src_entry))
src_button.pack()

dest_label = tk.Label(root, text="Destination Directory:")
dest_label.pack()
dest_entry = tk.Entry(root, width=50)
dest_entry.pack()
dest_button = ttk.Button(root, text="Browse", command=lambda: browse_directory(dest_entry))
dest_button.pack()

# Create entry widget and button for CSV file
csv_label = tk.Label(root, text="CSV File:")
csv_label.pack()
csv_entry = tk.Entry(root, width=50)
csv_entry.pack()
csv_button = ttk.Button(root, text="Browse", command=browse_csv)
csv_button.pack()

# Create OptionMenu for selecting operations
operation_var = tk.StringVar()
operation_var.set("Copy")  # default value
operation_menu = ttk.OptionMenu(root, operation_var, "Copy", "Copy", "Move", "Delete")
operation_menu.pack()

# Create button to initiate operations
perform_button = ttk.Button(root, text="Perform Operations", command=perform_operations)
perform_button.pack()

# Create a scrolled text area to display operation status
status_text = scrolledtext.ScrolledText(root, width=50, height=10)
status_text.pack()

root.mainloop()
