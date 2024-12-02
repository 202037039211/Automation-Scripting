import os
import shutil
from datetime import datetime

# Configuration
SOURCE_DIR = os.path.expanduser("path/to/source_dir")  # Change to your source directory
DESTINATION_DIR = os.path.expanduser("path/to/destination_dir")  # Change to your destination directory
LOG_FILE = os.path.expanduser("$DESTINATION_DIR/sync_log.txt")

def sync_directories():
    """
    Synchronizes files from the source directory to the destination directory.
    Only newer or missing files are copied. Sync actions are logged.
    """
    with open(LOG_FILE, "a") as log:
        for root, _, files in os.walk(SOURCE_DIR):
            # Calculate relative path
            rel_path = os.path.relpath(root, SOURCE_DIR)
            dest_path = os.path.join(DESTINATION_DIR, rel_path)

            # Create destination path if it doesn't exist
            os.makedirs(dest_path, exist_ok=True)

            # Sync files
            for file_name in files:
                source_file = os.path.join(root, file_name)
                destination_file = os.path.join(dest_path, file_name)

                # Copy file if it doesn't exist in destination or is newer
                if not os.path.exists(destination_file) or os.path.getmtime(source_file) > os.path.getmtime(destination_file):
                    shutil.copy2(source_file, destination_file)
                    log_entry = f"{datetime.now()}: Synced {source_file} to {destination_file}\n"
                    log.write(log_entry)
                    print(log_entry.strip())  # Display the sync action

if __name__ == "__main__":
    sync_directories()
