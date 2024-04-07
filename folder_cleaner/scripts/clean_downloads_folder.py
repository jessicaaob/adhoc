import os

file_path = '/Users/jessicaobrien/Downloads/Warp.dmg'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print('File has been successfully deleted')
else:
    print('This file does not exist')