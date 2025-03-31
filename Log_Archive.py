import argparse
import tarfile
import time
import os

# Function to archive log files
parser = argparse.ArgumentParser(description="Archive log files")
parser.add_argument("log_directory", type=str, help="Path to the log directory")
args = parser.parse_args()

# Check if the provided log directory exists
log_directory = args.log_directory
if not os.path.exists(log_directory):
    print(f"Error: The directory {log_directory} does not exist.")
    exit(1)

print(f"Archiving logs from {log_directory}")

# Get the current date and time for the archive name
timestamp = time.strftime("%Y%m%d-%H%M%S")
archive_name = f"logs_{timestamp}.tar.gz"

# Compress the log files into a tar.gz archive
archive_path = os.path.expanduser(r"C:\Users\lephia\Documents\Log_Archive")
try:
    print(f"Creating archive directory at: {archive_path}")
    os.makedirs(archive_path, exist_ok=True)
except PermissionError as e:
    print(f"Error: Unable to create the archive directory. {e}")
    exit(1)

# Create a tar.gz archive of the log directory
try:
    with tarfile.open(os.path.join(archive_path, archive_name), "w:gz") as archive:
        archive.add(log_directory, arcname=os.path.basename(log_directory))
except Exception as e:
    print(f"Error during archiving: {e}")
    exit(1)

# Print the path of the created archive
print(f"Logs archived to: {os.path.join(archive_path, archive_name)}")
print("Log archiving completed successfully.")

# Write the archive operation to the log file
log_file = os.path.join(archive_path, "archive_log.txt")
try:
    with open(log_file, "a") as f:
        f.write(f"{timestamp} - Archived logs to {archive_name}\n")
    print(f"Log file created at: {log_file}")
except Exception as e:
    print(f"Error writing to log file: {e}")
    exit(1)
