import os
import string
import shutil

def copy_file(src, dest):
    shutil.copyfile(src, dest)
    print(f"Copied contents from {src} to {dest}")
