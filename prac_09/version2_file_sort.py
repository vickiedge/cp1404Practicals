"""
Program to sort files with various name and extensions into subdirectories for each extension\
Version 2 - subdirectory folder names and extension sorting governed user input,
stored in dictionary (key=extensions, value=folders)
"""

import os
import shutil

print("Starting directory is: {}".format(os.getcwd()))
os.chdir('FilesToSort')
print(os.getcwd())
filenames = []
extension_to_category = {}
for name in os.listdir('.'):
    extension = name[name.find('.') + 1:]
    if name.find(extension):
        filenames.append(name)
        extension_to_category.update({extension:""})
for extension in extension_to_category.keys():
    category = input("What category would you like to sort {} files into? ".format(extension))
    if category not in extension_to_category.values():
        os.mkdir(category)
    extension_to_category.update({extension: category})
for name in filenames:
    if extension == extension_to_category.keys():
        shutil.move(extension , category + '/' + extension)
print(extension_to_category)
print(filenames)  

