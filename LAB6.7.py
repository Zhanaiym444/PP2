import os
import string
import shutil

def check_access(path):
    print(f"Exists: {os.access(path, os.F_OK)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")