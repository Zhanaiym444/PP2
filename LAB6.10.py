import os
import string
import shutil

def write_list_to_file(filename, data_list):
    with open(filename, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")
    print(f"List written to {filename}")