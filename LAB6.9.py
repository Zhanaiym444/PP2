import os
import string
import shutil

def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")