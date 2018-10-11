"""
Program to sort files with various name and extensions into subdirectories for each extension\
Version 1
"""

import os
import shutil

print("Starting directory is: {}".format(os.getcwd()))
os.chdir('FilesToSort')
print(os.getcwd())
extensions = []
for name in os.listdir('.'):
    extension = name[name.find('.') + 1:]
    if extension not in extensions:
        extensions.append(extension)
        os.mkdir(extension)
    shutil.move(name, extension + '/' + name)
    print(extension)
