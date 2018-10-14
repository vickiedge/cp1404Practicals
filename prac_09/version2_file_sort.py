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
extensions = []
for name in os.listdir('.'):
    extension = name[name.find('.') + 1:]
    if extension not in extensions:
        extensions.append(extension)
categories = []
for extension in extensions:
    category = input("Wnat category would you like to sort {} files into? ".format(extension))
    categories.append(category)
#   print(extensions, categories)
extension_to_category = dict(zip(extensions, categories))
# print(extension_to_category)
for name in os.listdir('.'):
    if name[name.find('.') + 1:] == extension_to_category(extensions):
         print(name, category)

#     if extension not in extensions:
#         extensions.append(extension)
#         os.mkdir(extension)
#     shutil.move(name, extension + '/' + name)
#     print(extension)
#
# os.mkdir(categories)
#
