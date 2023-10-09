import os
import zipfile
import re

# Directory where the zipped files are located
source_directory = r'C:\Users\hzs0084\Downloads\submissions'

#Creates the lab folder for me in the file path

path= r'C:\Users\hzs0084\Downloads\ISMN-3080 Submissions'

os.chdir(path)

createsfolder = 'Lab 4' #Update the string to reflect the name of the folder
if not os.path.exists(createsfolder):      #Update the path as well otherwise the Path won't exist
    os.makedirs(createsfolder)

# Directory where you want to extract the contents
#put r in front of a normal string so that it can convert the string to a raw string
target_directory = r'C:\Users\hzs0084\Downloads\ISMN-3080 Submissions\PA 4'

# Regular expression pattern to match the username in the zip file name
username_pattern = r'_([a-zA-Z]{3}\d{4})_'

# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    # Check if the file is a zip file
    if filename.endswith('.zip'):
        # Extract the username from zip file name
        match = re.search(username_pattern, filename)
        if match:
            username = match.group(1)
            # Construct the target folder path based on the username
            target_folder = os.path.join(target_directory, username)
            
            # Create the target folder if it doesn't exist
            os.makedirs(target_folder, exist_ok=True)
            
            # Extract the contents of the zipped file to the target folders
            with zipfile.ZipFile(os.path.join(source_directory, filename), 'r') as zip_ref:
                zip_ref.extractall(target_folder)
                print(f"Extracted contents of {filename} to {target_folder}")
