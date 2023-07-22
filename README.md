# Folder Cleaner
## Automatic File Cleanup

This Python script is designed to automatically clean up files in a specified folder based on their last access time. It will check the last access time of each file in the folder and delete files that haven't been accessed within the last 30 days.

## Configuration

Before running the script, make sure to set the `folder_path` variable to the path of the folder you want to clean up. Replace `"path/to/folder"` with the actual folder path.

## Usage

1. Save the script in a Python file, e.g., `file_cleanup.py`.
2. Set the `folder_path` variable to the path of the folder you want to clean up.
3. Run the script in your preferred Python environment.

## Note

- The script uses the `os` and `datetime` modules to determine the last access time of each file and calculate the time difference.
- Files that haven't been accessed within the last 30 days will be deleted.
- Be cautious while using this script, as deleted files cannot be easily recovered.
- Make sure to test the script on a test folder before running it on important data.

Enjoy using this automatic file cleanup script to keep your folder organized!
