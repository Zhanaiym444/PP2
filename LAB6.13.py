import os
import string
import shutil

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File {path} deleted successfully.")
        else:
            print("No permission to delete the file.")
    else:
        print("File does not exist.")
