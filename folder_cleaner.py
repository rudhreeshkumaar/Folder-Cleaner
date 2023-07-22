import os
import datetime

folder_path = "path/to/folder"  # replace with your folder path

# get the current time
now = datetime.datetime.now()

# iterate over all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        # get the file's last access time
        last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(file_path))
        # calculate the difference between the current time and the last access time
        time_diff = now - last_access_time
        # check if the file hasn't been accessed in more than 30 days
        if time_diff.days > 30:
            # delete the file
            os.remove(file_path)
