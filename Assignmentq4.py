import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' not found.")

        os.makedirs(dest_dir, exist_ok=True)

        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            while os.path.exists(dest_path):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                dest_path = os.path.join(dest_dir, f"{os.path.splitext(filename)[0]}_{timestamp}{os.path.splitext(filename)[1]}")

            shutil.copy2(source_path, dest_path)
            print(f"Copied: {source_path} to {dest_path}")

        print("Backup completed successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory, destination_directory = sys.argv[1], sys.argv[2]

    backup_files(source_directory, destination_directory)
