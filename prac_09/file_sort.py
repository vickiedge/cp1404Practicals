"""
Program to sort files with various name and extensions into subdirectories for each extension
"""

import os

print("Starting directory is: {}".format(os.getcwd()))
os.chdir('FilesToSort')
print(os.getcwd())
os.mkdir('txt')
names = [name for name in os.listdir('.') if name.endswith('.txt')]
for name in names:
    shutil.move(filename, 'temp/' + name)
    print(name)



