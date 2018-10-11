"""
Program to sort files with various name and extensions into subdirectories for each extension
"""

import os
import shutil

print("Starting directory is: {}".format(os.getcwd()))
os.chdir('FilesToSort')
print(os.getcwd())
# os.mkdir('txt')
# names = [name for name in os.listdir('.') if name.endswith('.txt')]
extensions=[]
for name in os.listdir('.'):
    # shutil.move(name, 'temp/' + name)
    extension = name[name.find('.')+1:]
    if extension not in extensions:
        extensions.append(extension)
        os.mkdir(extension)
    shutil.move(name, extension+'/' + name)
    print(extension)



