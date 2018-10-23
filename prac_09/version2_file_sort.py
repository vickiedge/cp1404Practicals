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
# create lookup table for where extensions go
extension_to_category = {}
for name in os.listdir('.'):
    extension = name[name.find('.') + 1:]
    # this if statement is only for extensions not seen before
    if extension not in extension_to_category:
        category = input("What category would you like to sort {} files into? ".format(extension))
        extension_to_category[extension] = category
        # if category not in extension_to_category.values():
        try:
            os.mkdir(category)
        except:
            pass
    print(name, extension_to_category[extension] + '/' + name)
    shutil.move(name, extension_to_category[extension] + '/' + name)
print(extension_to_category)
