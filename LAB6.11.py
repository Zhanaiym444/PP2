import os
import string
import shutil

def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as file:
            file.write(f"This is file {letter}.txt")
    print("A–Z files created.")