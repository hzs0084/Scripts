# # importing the zipfile module
# from zipfile import ZipFile
# from os import path

# import os

# # loading the test.zip and creating a zip object
# with ZipFile("C:\\Users\\hzs0084\\Downloads\\test.zip", 'r') as zObject:

# 	# Extracting all the members of the zip
# 	# into a specific location.
# 	zObject.extractall(
# 		path="C:\\Users\\hzs0084\\Downloads\\test")

import os

# Get the path to the folder
folder_path = "C:\\Users\\hzs0084\\Downloads\\Test_name"

# Get the name of the folder
folder_name = os.path.basename(folder_path)

# Split the name of the folder into a list of words
words = folder_name.split()

# Reverse the order of the words in the list
words.reverse()

print(words)

# Join the words back together to form a new name
new_name = " ".join(words)

# Create a new folder with the new name
os.mkdir(os.path.join(folder_path, new_name))